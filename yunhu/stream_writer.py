import httpx
import threading
import queue
from typing import Optional, Generator


class StreamWriter:
    def __init__(self, token: str, recv_id: str, recv_type: str, content_type: str, base_url: str):
        self.token = token
        self.recv_id = recv_id
        self.recv_type = recv_type
        self.content_type = content_type
        self.base_url = base_url
        self._queue: queue.Queue = queue.Queue()
        self._closed = False
        self._response: Optional[httpx.Response] = None
        self._error: Optional[Exception] = None
        self._thread: Optional[threading.Thread] = None
        self._started = False

    def _generate(self) -> Generator[bytes, None, None]:
        while True:
            try:
                chunk = self._queue.get(timeout=0.1)
                if chunk is None:
                    break
                yield chunk
            except queue.Empty:
                if self._closed:
                    break
                continue

    def _send_request(self):
        url = f"{self.base_url}/bot/send-stream"
        params = {
            "token": self.token,
            "recvId": self.recv_id,
            "recvType": self.recv_type,
            "contentType": self.content_type
        }
        try:
            with httpx.Client() as client:
                self._response = client.post(
                    url,
                    params=params,
                    content=self._generate(),
                    headers={
                        "Content-Type": "text/plain",
                    },
                    timeout=60.0
                )
        except Exception as e:
            self._error = e
            print(f"流式请求错误: {e}")

    def write(self, data):
        if self._closed:
            raise RuntimeError("StreamWriter is closed")
        
        if not self._started:
            self._started = True
            self._thread = threading.Thread(target=self._send_request, daemon=True)
            self._thread.start()
        
        if isinstance(data, str):
            data = data.encode('utf-8')
        self._queue.put(data)

    def close(self):
        if self._closed:
            return
        self._closed = True
        self._queue.put(None)
        if self._thread:
            self._thread.join(timeout=30)

    def get_response(self) -> Optional[dict]:
        if self._response:
            try:
                return self._response.json()
            except:
                return {"status": self._response.status_code, "text": self._response.text}
        return None

    def get_error(self) -> Optional[Exception]:
        return self._error

import json
import requests


class Openapi(object):
    """
    开放接口，用于发送消息。
    """
    baseUrl = "https://chat-go.jwzhd.com/open-apis/v1"

    def __init__(self, token: str) -> None:
        self.token = token

    class Messages:
        def __init__(self, outer_instance):
            self.outer_instance = outer_instance

        def sendTextMessage(self, recvId: str, recvType: str, content: map):
            """
            单条，发送文本消息
            """
            return self.sendMessage(recvId, recvType, "text", content)

        def sendMarkdownMessage(self, recvId: str, recvType: str, content: map):
            """
            单条，发送markdown消息
            """
            return self.sendMessage(recvId, recvType, "markdown", content)

        def sendMessage(self, recvId: str, recvType: str, contentType: str, content: dict):
            """
            单条，发送单条消息
            """
            params = {
                "recvId": recvId,
                "recvType": recvType,
                "contentType": contentType,
                "content": content
            }
            headers = {'Content-Type': 'application/json'}
            return requests.post(f"{Openapi.baseUrl}/bot/send?token={self.outer_instance.token}", headers=headers,
                                 data=json.dumps(params))

        def batchSendTextMessage(self, recvIds: list, recvType: str, content: dict):
            """
            批量，发送文本消息
            """
            return self.batchSendMessage(recvIds, recvType, "text", content)

        def batchSendMarkdownMessage(self, recvIds: list, recvType: str, content: dict):
            """
            批量，发送markdown消息
            """
            return self.batchSendMessage(recvIds, recvType, "markdown", content)

        def batchSendMessage(self, recvIds: list, recvType: str, contentType: str, content: dict):
            """
            批量，批量发送消息
            """
            params = {
                "recvIds": recvIds,
                "recvType": recvType,
                "contentType": contentType,
                "content": content
            }
            headers = {'Content-Type': 'application/json'}
            return requests.post(f"{Openapi.baseUrl}/bot/batch_send?token={self.outer_instance.token}", headers=headers,
                                 data=json.dumps(params))

        def editMessage(self, msgId: str, recvId: str, recvType: str, contentType: str, content: dict):
            """
            单条，编辑单条消息
            """
            params = {
                "msgId": msgId,
                "recvId": recvId,
                "recvType": recvType,
                "contentType": contentType,
                "content": content
            }
            headers = {'Content-Type': 'application/json'}
            return requests.post(f"{Openapi.baseUrl}/bot/edit`?token={self.outer_instance.token}", headers=headers,
                                 data=json.dumps(params))

    class Board:
        def __init__(self, outer_instance):
            self.outer_instance = outer_instance

        def setBoard(self, recvId: str, recvType: str, contentType: str, content: str):
            """
            设置某用户的看板内容
            """
            params = {
                "recvId": recvId,
                "recvType": recvType,
                "contentType": contentType,
                "content": content
            }
            headers = {'Content-Type': 'application/json; charset=utf-8'}
            requests.post(f"{Openapi.baseUrl}/bot/board?token={self.outer_instance.token}", headers=headers,
                          data=json.dumps(params))

        def setAllUserBoard(self, contentType: str, content: str):
            """
            设置所有用户的看板内容
            """
            params = {
                "contentType": contentType,
                "content": content
            }
            headers = {'Content-Type': 'application/json; charset=utf-8'}
            requests.post(f"{Openapi.baseUrl}/bot/board-all?token={self.outer_instance.token}", headers=headers,
                          data=json.dumps(params))

        def CancelBoard(self, recvId: str, recvType: str):
            """
            取消用户的看板
            """
            params = {
                "recvId": recvId,
                "recvType": recvType
            }
            headers = {'Content-Type': 'application/json; charset=utf-8'}
            requests.post(f"{Openapi.baseUrl}/bot/board-dismiss?token={self.outer_instance.token}", headers=headers,
                          data=json.dumps(params))

        def CancelAllUserBoard(self):
            requests.post(f"{Openapi.baseUrl}/bot/board-all-dismiss?token={self.outer_instance.token}")

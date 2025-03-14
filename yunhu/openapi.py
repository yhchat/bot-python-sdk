
import json
import requests


class Openapi(object):
    """
    开放接口，用于发送消息。
    """
    baseUrl = "https://chat-go.jwzhd.com/open-apis/v1"

    def __init__(self, token: str) -> None:
        self.token = token

    def sendTextMessage(self, recvId: str, recvType: str, content: dict):
        """
        单条，发送文本消息
        """
        return self.sendMessage(recvId, recvType, "text", content)

    def sendMarkdownMessage(self, recvId: str, recvType: str, content: dict):
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
        return requests.post(self.baseUrl + '/bot/send?token=' + self.token,headers=headers, data=json.dumps(params))

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
        batchCount = 200
        recvIdss =  [recvIds[i:i+batchCount] for i in range(0, len(recvIds), batchCount)]
        resList = []
        for l in recvIdss:
            params = {
                "recvIds": l, 
                "recvType": recvType, 
                "contentType": contentType, 
                "content": content
            }
            headers = {'Content-Type': 'application/json'}
            res = requests.post(self.baseUrl + '/bot/batch_send?token=' + self.token,headers=headers, data=json.dumps(params))
            resList.append(res)
        return resList

    
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
        return requests.post(self.baseUrl + '/bot/edit?token=' + self.token,headers=headers, data=json.dumps(params))
    
    def SetBotBoard(self, chatId: str, chatType: str,memberId: str, contentType: str, content: str, expireTime: int):
        """
        @description: 机器人看板设置接口
        机器人看板类型contentType取值: text、markdown、html
        expireTime: 看板过期时间，11位时间戳。比如过期时间为10分钟，则expireTime为当前时间戳+600秒（int(time.time()) + 600）。
        """
        params = {
            "chatId": chatId, 
            "recvType": chatType, 
            "memberId": memberId, 
            "contentType": contentType, 
            "content": content, 
            "expireTime": expireTime
         }
        headers = {'Content-Type': 'application/json'}
        return requests.post(self.baseUrl + '/bot/board?token=' + self.token,headers=headers, data=json.dumps(params))
    
    def SetBotBoardAll(self, contentType: str, content: str, expireTime: int):

        """
        @description: 机器人看板批量设置接口
        机器人看板类型contentType取值: text、markdown、html
        expireTime: 看板过期时间，11位时间戳。比如过期时间为10分钟，则expireTime为当前时间戳+600秒（int(time.time()) + 600）。
        """
        params = {
            "contentType": contentType, 
            "content": content, 
            "expireTime": expireTime
         }
        headers = {'Content-Type': 'application/json'}
        return requests.post(self.baseUrl + '/bot/board-all?token=' + self.token,headers=headers, data=json.dumps(params))
    
    def DismissBotBoard(self, chatId: str, chatType: str,memberId: str):
        """
        @description: 机器人看板取消接口
        """
        params = {
            "chatId": chatId, 
            "recvType": chatType, 
            "memberId": memberId, 
         }
        headers = {'Content-Type': 'application/json'}
        return requests.post(self.baseUrl + '/bot/board-dismiss?token=' + self.token,headers=headers, data=json.dumps(params))
    
    def DismissBotBoardAll(self):
        """
        @description: 机器人看板取消接口
        """
        params = {}
        headers = {'Content-Type': 'application/json'}
        return requests.post(self.baseUrl + '/bot/board-all-dismiss?token=' + self.token,headers=headers, data=json.dumps(params))
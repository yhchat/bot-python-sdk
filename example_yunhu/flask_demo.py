from flask import Flask, request
import json
import requests
from yunhu.subscription import Subscription
from yunhu.openapi import Openapi


app = Flask(__name__)
sub = Subscription()
openapi = Openapi("xxx")

@app.route('/sub',methods = ['POST'])
def subRoute():
   if request.method == 'POST':
      sub.listen(request)
      return "success"

@sub.onMessageNormal
def onMessageNormalHander(event):
   print("onMessageNormalSubscriber")
   print(event)
   res = openapi.sendMessage(event["sender"]["senderId"], event["sender"]["senderType"], "text", {"text": "机器人回复普通消息"})
   print(res.content)
   
   content = {
      "text": "机器人批量回复普通消息",
      "buttons": [
         {
            "text": "复制内容1",
            "actionType": 2,
            "value": "复制内容1",
         },
         {
            "text": "复制内容2",
            "actionType": 2,
            "value": "复制内容2",
         },
      ],
   }

   res2 = openapi.batchSendMessage([event["sender"]["senderId"]], event["sender"]["senderType"], "text", content)
   print(res2.content)

@sub.onMessageInstruction
def onMessageInstructionHandler(event):
   print("onMessageInstructionlSubscriber")
   print(event)
   res = openapi.editMessage("xxx", event["sender"]["senderId"], event["sender"]["senderType"], "text", {"text": "机器人编辑消息"})
   print(res.content)

@sub.onGroupJoin
def onGroupJoinHandler(event):
   print("onGroupJoinSubscriber")
   print(event)

@sub.onGroupLeave
def onGroupLeaveHandler(event):
   print("onGroupLeaveSubscriber")
   print(event)

@sub.onBotFollowed
def onBotFollowedHandler(event):
   print("onBotFollowedSubscriber")
   print(event)

@sub.onBotUnfollowed
def onBotUnfollowedHandler(event):
   print("onBotUnfollowedSubscriber")
   print(event)

@sub.onButtonReportInline
def onButtonReportInlineHandler(event):
   print("onButtonReportInlineSubscriber")
   print(event)

if __name__ == '__main__':
   app.run("0.0.0.0", 8857)

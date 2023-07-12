from flask import Flask, request
from yunhu.subscription import Subscription
from yunhu.openapi import Openapi

app = Flask(__name__)
sub = Subscription()
api = Openapi("71fd5414100748eda678e09763122e53")
Messages = Openapi.Messages(api)
Board = Openapi.Board(api)


@app.route('/sub', methods=['POST'])
def subRoute():
    if request.method == 'POST':
        sub.listen(request)
        return "success"


@sub.onMessageNormal
def onMessageNormalHander(event):
    print("onMessageNormalSubscriber")
    print(event)
    res = Messages.sendMessage(event["sender"]["senderId"], event["sender"]["senderType"], "text",
                               {"text": "Hello World"})
    print(res.content)

    content = {
        "text": "机器人批量回复普通消息",
        "buttons": [
            {
                "text": "取消看板",
                "actionType": 3,
                "value": "CancelBoard",
            },
            {
                "text": "复制消息",
                "actionType": 2,
                "value": event["message"]["content"]["text"],
            },
        ],
    }

    Board.setBoard(event["sender"]["senderId"], "user", "text", event["message"]["content"]["text"])
    res2 = Messages.batchSendMessage([event["sender"]["senderId"]], event["sender"]["senderType"], "text",
                                     content)
    print(res2.content)


@sub.onMessageInstruction
def onMessageInstructionHandler(event):
    print("onMessageInstructionlSubscriber")
    print(event)
    res = Messages.editMessage("xxx", event["sender"]["senderId"], event["sender"]["senderType"], "text",
                               {"text": "机器人编辑消息"})
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
    if event["value"] == "CancelBoard":
        # Board.CancelAllUserBoard() # <--取消所有用户的看板
        Board.CancelBoard(event["recvId"], "recvType")  # <--取消某用户的看板


if __name__ == '__main__':
    app.run("0.0.0.0", 7888)

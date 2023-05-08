class Subscription(object):
    """
    订阅事件类
    """
    onMessageNormalSubscriber = None
    onMessageInstructionSubscriber = None
    onGroupJoinSubscriber = None
    onGroupLeaveSubscriber = None
    onBotFollowedSubscriber = None
    onBotUnfollowedSubscriber = None
    onButtonReportInlineSubscriber = None

    def __init__(self) -> None:
        pass

    def listen(self, request):

        eventType = request.get_json()['header']['eventType']
        event = request.get_json()["event"]

        if eventType == 'message.receive.normal': # 普通消息事件  
            self.onMessageNormalSubscriber(event)
        elif eventType == 'message.receive.instruction': # 指令消息事件 
            self.onMessageInstructionSubscriber(event)
        elif eventType == 'group.join': # 加入群组事件 
            self.onGroupJoinSubscriber(event)
        elif eventType == 'group.leave': # 退出群组事件 
            self.onGroupLeaveSubscriber(event)
        elif eventType == 'bot.followed': # 关注机器人事件 
            self.onBotFollowedSubscriber(event)
        elif eventType == 'bot.unfollowed': # 取消关注机器人事件  
            self.onBotUnfollowedSubscriber(event)
        elif eventType == 'button.report.inline': # 消息下按钮点击回调事件 
            self.onButtonReportInlineSubscriber(event)

    def onMessageNormal(self, func):
        self.onMessageNormalSubscriber = func
        return func

    def onMessageInstruction(self, func):
        self.onMessageInstructionSubscriber = func
        return func

    def onGroupJoin(self, func):
        self.onGroupJoinSubscriber = func
        return func

    def onGroupLeave(self, func):
        self.onGroupLeaveSubscriber = func
        return func

    def onBotFollowed(self, func):
        self.onBotFollowedSubscriber = func
        return func

    def onBotUnfollowed(self, func):
        self.onBotUnfollowedSubscriber = func
        return func

    def onButtonReportInline(self, func):
        self.onButtonReportInlineSubscriber = func
        return func
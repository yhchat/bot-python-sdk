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
    onBotShortcutMenuEventSubscriber = None

    def __init__(self) -> None:
        pass

    def listen(self, request):

        eventType = request.get_json()['header']['eventType']
        event = request.get_json()["event"]

        if eventType == 'message.receive.normal' and self.onMessageNormalSubscriber != None: # 普通消息事件  
            self.onMessageNormalSubscriber(event)
        elif eventType == 'message.receive.instruction' and self.onMessageInstructionSubscriber != None: # 指令消息事件 
            self.onMessageInstructionSubscriber(event)
        elif eventType == 'group.join' and self.onGroupJoinSubscriber != None: # 加入群组事件 
            self.onGroupJoinSubscriber(event)
        elif eventType == 'group.leave' and self.onGroupLeaveSubscriber != None: # 退出群组事件 
            self.onGroupLeaveSubscriber(event)
        elif eventType == 'bot.followed' and self.onBotFollowedSubscriber != None: # 关注机器人事件 
            self.onBotFollowedSubscriber(event)
        elif eventType == 'bot.unfollowed' and self.onBotUnfollowedSubscriber != None: # 取消关注机器人事件  
            self.onBotUnfollowedSubscriber(event)
        elif eventType == 'button.report.inline' and self.onButtonReportInlineSubscriber != None: # 消息下按钮点击回调事件 
            self.onButtonReportInlineSubscriber(event)
        elif eventType == 'bot.shortcut.menu' and self.onBotShortcutMenuEventSubscriber != None: # 机器人快捷菜单按钮事件 
            self.onBotShortcutMenuEventSubscriber(event)

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

    def onBotShortcutMenuEvent(self, func):
        self.onBotShortcutMenuEventSubscriber = func
        return func
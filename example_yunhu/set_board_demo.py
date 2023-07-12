from yunhu.openapi import Openapi


def main():
    openapi = Openapi("xxx")
    res = openapi.SetBotBoardAll("text", "py测试")
    print(res.content)
    
    
if __name__ == '__main__':
    main()
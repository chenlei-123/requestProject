import requests


class Base:
    def __init__(self):
        # 获取token的接口,corpid 企业id，corpsecret，管理工具，通讯录工具，Secret
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww566a45cc18b674b4&corpsecret=ZqPQxd_gT0MbSZW9IVfW2eitGwxsB5DIFSUT5x0hpCM'
        r = requests.get(url).json()
        self.token = r['access_token']
        # 声明一个session
        self.request_session = requests.Session()
        # 把token放入到session中,每次参数都有token
        self.request_session.params = {'access_token': self.token}

    def send(self, *args, **kwargs):
        # 用 session
        r = self.request_session.request(*args, **kwargs)
        return r.json()

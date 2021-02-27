import requests


def test_add_member():
    # 获取token的接口,corpid 企业id，corpsecret，管理工具，通讯录工具，Secret
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww566a45cc18b674b4&corpsecret=ZqPQxd_gT0MbSZW9IVfW2eitGwxsB5DIFSUT5x0hpCM'
    r = requests.get(url)
    print(r.json()['access_token'])
    token = r.json()['access_token']

    # 数据清理
    # 删除成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=zhangsan"
    r = requests.get(url)
    print(r.json())

    # 创建成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
    body = {
        "userid": "zhangsan",
        "name": "张三",
        "mobile": "+86 13800000001",
        "department": [1]
    }
    r = requests.post(url, json=body)
    print(r.json())

    # 获取成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=ChenLei"
    r = requests.get(url)
    print(r.json())


def test_delete_member():
    # 数据清理（数据准备）
    # 创建成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
    body = {
        "userid": "zhangsan",
        "name": "张三",
        "mobile": "+86 13800000001",
        "department": [1]
    }
    r = requests.post(url, json=body)
    print(r.json())

    # 获取成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=ChenLei"
    r = requests.get(url)
    print(r.json())


    # 删除成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=zhangsan"
    r = requests.get(url)
    print(r.json())
    pass



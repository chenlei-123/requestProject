import requests


def test_demo():
    # 获取token的接口,corpid 企业id，corpsecret，管理工具，通讯录工具，Secret
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww566a45cc18b674b4&corpsecret=ZqPQxd_gT0MbSZW9IVfW2eitGwxsB5DIFSUT5x0hpCM'
    r = requests.get(url)
    print(r.json()['access_token'])
    token = r.json()['access_token']

    # 读取成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=ChenLei"
    r = requests.get(url)
    print(r.json())

    # 更新成员信息
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}"
    body = {
        "userid": "ChenLei",
        "name": "陈磊1111"
    }
    header = {"cpntent-type": "application/json"}
    r = requests.post(url, data=body, headers=header)
    print(r.json())

    #     创建成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
    body = {
        "userid": "zhangsan",
        "name": "张三",
        "mobile": "+86 13800000001",
        "department": [1]
    }
    r = requests.post(url, json=body)
    print(r.json())

    # 删除成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=zhangsan"
    r = requests.get(url)
    print(r.json())

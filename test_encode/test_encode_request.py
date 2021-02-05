import requests
import base64
import json

class ApiRequest:

    def send(self, data: dict):
        res = requests.request(data['method'], data['url'], headers=data['headers'])
        if data['encoding'] == 'base64':
            return json.loads(base64.b64decode(res.content))
        # 把加密后的响应值发给第三方服务，让第三方做解密然后返回解密后的信息
        elif data['encoding'] == 'private':
            return requests.post('url', data=res.content)

def test_encode():
    url = 'http://127.0.0.1:9999/demo1.txt'
    r = requests.get(url=url)
    res = json.loads(base64.b64decode(r.content))
    print(res)


def test_send():
    req_data = {
        'method': 'get',
        'url': 'http://127.0.0.1:9999/demo1.txt',
        'headers': None,
        'encoding': 'base64'
    }
    ar = ApiRequest()
    print(ar.send(req_data))

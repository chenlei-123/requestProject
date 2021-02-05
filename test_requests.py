import requests
from requests.auth import HTTPBasicAuth


def test_demo():
    url = "https://httpbin.ceshiren.com/cookies"
    header = {"User-Agent": "hogwarts"}
    cookie_data = {"hogwarts": "school",
                   "teacher": "chenlei"}
    r = requests.get(url=url, headers=header, cookies=cookie_data)
    print(r.request.headers)


def test_oauth():
    r = requests.get(url="https://httpbin.ceshiren.com/basic-auth/chenlei/123", auth=HTTPBasicAuth("chenlei", "123"))
    print(r.text)

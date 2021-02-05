import requests
from jsonpath import jsonpath
from hamcrest import *
class TestDemo:
    def test_get(self):
        r = requests.get('https://httpbin.ceshiren.com/get')
        print(r.text)
        print(r.json())
        print(r.status_code)

    def test_query(self):
        payload = {"level": 1, "name": "chenlei"}
        r = requests.get("https://httpbin.ceshiren.com/get", params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post(self):
        payload = {"level": 1, "name": "chenlei"}
        r = requests.post("https://httpbin.ceshiren.com/post", data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_header(self):
        r = requests.get("https://httpbin.ceshiren.com/get", headers={"h": "header"})
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200
        assert r.json()['headers']["H"] == "header"

    def test_post_json(self):
        payload = {"level": 1, "name": "chenlei"}
        r = requests.post("https://httpbin.ceshiren.com/post", json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['level'] == 1

    def test_hogwarts_json(self):
        r = requests.get("https://ceshiren.com/categories.json")
        print(r.text)
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == '开源项目'
        print(jsonpath(r.json(), '$..name'))
        assert jsonpath(r.json(), '$..name')[0] == '开源项目'

    def test_hamcrest(self):
        r = requests.get("https://ceshiren.com/categories.json")
        print(r.text)
        assert r.status_code == 200
        assert_that(r.json()['category_list']['categories'][0]['name'],equal_to('开源项目'))

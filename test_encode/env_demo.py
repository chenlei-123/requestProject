import requests
import yaml


class Api:
    env = yaml.safe_load(open("env.yaml"))

    # data是一个请求信息
    def send(self, data: dict):
        data["url"] = str(data["url"]).replace("testing-studio", self.env["testing-studio"][self.env["default"]])
        r = requests.request(method=data["method"], url=data["url"], headers=data["headers"])
        return r


def test_api():
    data = {
        "method": "get",
        "url": "http://testing-studio:9999/demo1.txt",
        "headers": None
    }
    api = Api()
    print(api.send(data))

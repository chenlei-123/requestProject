from mitmproxy import ctx
from mitmproxy import http


class ABC:
    def __init__(self):
        self.num = 0

    def request(self, flow: http.HTTPFlow) -> None:
        if "/v5/stock/batch/quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
            with open(r"test.json", 'r', encoding="utf-8") as f:
                flow.response = http.HTTPResponse.make(
                    200,  # (optional) status code
                    f.read(),  # (optional) content
                    {"Content-Type": "application/json"}  # (optional) headers
                )


addons = [
    ABC()
]

# mitmproxy -s proxy.py -p 8080
# mitmdump -s proxy.py -p 8080

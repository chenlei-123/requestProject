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


def test_request():
    url = "https://fastlend.yuanzidai.com/yzd/v540/account/login"

    payload = "sec_level=2&data=2bixr%2BgxXxWCh5Rev6nDPx7xLwHaUHuyRUKwY0d5cJt8q9BU8jOapKDcVVBTTJVPrA599b7pMgOg39a2r8knumapuKNEGsSWBIEO%2FH6yprED%2B3FWB5P%2BaR2ONC%2FW87liZQe1Xx6eviixis0HcnA%2BJEx%2BCS17z6JKZtjjiN6FQ%2BzxngkHSHAfh5%2FSojEZ2PeH1cXc%2FVHCYcEyITA4u6P%2FX7X7kP5smfnAjPbrijX2Jcf1src5gV%2BPok5X6UgltEiy%2FmglUf%2B60lMDt%2BBSkzzmqWoSkD%2B18E8T9Q8%2B2jnvfCCcAIpGFBFQrWJL9veNt5VBO%2BnVBBNIVskgdAsSNPA%2BRwZCt%2BclWpWMkMp3A7oSEfzZ9s4UzPtMR1AmJrsEGu2obVXQkqSgqUjVy6CCWDI6ik6wvjmZ4rxLJoZqsqEjxV8IT33zcrJRMTNvOHUq5SuFILl9RuoYqufFyExnyN42z3gbrRUluqwliUZtFzxOJa%2FmOM66a5CmzEOkzxyM2k%2FOQqTWSdvxY5%2FvsHRZJbUEto32m3Vyb2n%2ByG80VRVWPcMUXYrXnL5BWXy4LuAXzc%2B3z9Se5XStxtoKfi64QdansNqS0brAxZICtKEvrsDyDt4SANDkYj5piSrFmEz69aO81HTNyk%2B5QFtp%2BCi9iJw2tl%2BAUeIG%2F88TuNheQZWXO5Y%3D&uid=0&ticket=&appid=2"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'rongid': "926397d750cfb589aea23d5090a643ca",
        'abclass': "1614760145_75",
        'host': "fastlend.yuanzidai.com",
        'user-agent': "okhttp/3.12.0",
        'cache-control': "no-cache",
        'postman-token': "f5129202-92aa-2afb-1b95-47ab9e8c4a14"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.json())

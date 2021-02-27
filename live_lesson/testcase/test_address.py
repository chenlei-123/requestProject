import pytest

from live_lesson.api.address import Address


class TestAddress:

    def setup(self):
        self.address = Address()

    @pytest.mark.parametrize("userid,mobile", [("lisi001232", "13511113333"),
                                               ("lisi001234", "13511114444"),
                                               ("lisi001267", "13511115555")])
    def test_add_member(self, userid, mobile):
        name = "今天星期六27"
        department = [1]
        self.address.delete_member(userid)
        r = self.address.add_member(userid=userid, name=name, mobile=mobile, department=department)
        assert r.get("errcode") == 0
        assert r.get("errmsg") == "created"
        r = self.address.get_member(userid)
        assert r.get("name", "userid 添加失败") == name

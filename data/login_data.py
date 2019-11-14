"""
------------------------------------
@Time : 2019/11/4
@Auth : Tian
@File : login_data.py
@IDE  : PyCharm
------------------------------------
"""


class LoginData(object):
    """用户登录测试数据"""

    login_success_data = [
        (
            "autotestsst",
            "Dublin13",
            "autotestsst@126.com"
        )
    ]

    login_fail_data = [
        (
            "autotestsst",
            "",
            "请输入密码，账号或密码错误"
        ),
        (
            "",
            "Dublin13",
            "请输入帐号，账号或密码错误"
        ),
        #(
        #    "tmao",
        #    "Dublin",
        #    "帐号或密码错误"
        #)
    ]


if __name__ == '__main__':
    pass

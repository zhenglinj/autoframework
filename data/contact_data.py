"""
------------------------------------
@Time : 2019/11/4
@Auth : Tian
@File : contact_data.py
@IDE  : PyCharm
------------------------------------
"""


class ContactData(object):
    """添加联系人测试数据"""

    add_contact_success = [
        (
            "tmao",
            "tmaostats@163.com",
            "1",
            "18267182508",
            "添加联系人1",
            "tmaostats@163.com"
        )
    ]
    add_contact_fail = [
        (
            "tmao2",
            "@163.com",
            "0",
            "18267182510",
            "添加联系人2",
            "请正确填写邮件地址。"
        )
    ]


if __name__ == '__main__':
    pass

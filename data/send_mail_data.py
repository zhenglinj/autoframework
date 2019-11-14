"""
------------------------------------
@Time : 2019/11/4
@Auth : Tian
@File : send_mail_data.py
@IDE  : PyCharm
------------------------------------
"""
from config.conf import *

class SendMailData(object):
    """发送邮件测试数据"""

    send_mail_success = [
        (
            "tmaostats1@163.com",
            "测试发送普通测试邮件",
            "测试发送普通测试邮件",
            "",
            "发送成功"
        ),
        (
            "tmaostats1@163.com",
            "测试发送带附件的邮件",
            "测试发送带附件的邮件",
            projectDir + "\\data\\attachment",
            "发送成功"
        ),
        (
            "tmaostats1@163.com",
            "",
            "测试发送带附件的邮件且主题为空",
            projectDir + "\\data\\attachment",
            "发送成功"
        )
    ]

    send_fail_address_is_none = [
        #(
        #    "",
        #    "测试收件人地址为空",
        #    "测试收件人地址为空",
        #    projectDir + "\\data\\attachment",
        #    "请填写收件人地址后再发送"
        #)
    ]

    send_fail_subject_is_none_data = [
        (
            "tmaostats@163.com",
            "",
            "测试邮件主题为空:不能添加附件",
            "",
            "确定真的不需要写主题吗？"
        )
    ]

    send_fail_address_is_invalid_data = [
        (
            "tmaostats",
            "测试收件人格式不正确",
            "测试收件人格式不正确",
            "",
            "以下邮箱地址无效，将无法成功收到邮件"
        )
    ]


if __name__ == '__main__':
    pass

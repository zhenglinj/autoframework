"""
----------------------------------
@Time: 2019/11/04
@Author: Tian
@Files: RunTestCase.py
@IDE: Pycharm
----------------------------------
"""
import sys
import pytest

from config.conf import *
from util.sendMailForReprot import SendMailWithReport


def main():
    if projectDir not in sys.path:
        sys.path.append(projectDir)
    # 执行用例
    os.system(args)
    # 发送邮件 这里我屏蔽了 自己添加自己的邮箱信息
    SendMailWithReport.send_mail(
        smtpServer, fromUser, fromPassWord, toUser, subject, contents, htmlName
    )


if __name__ == '__main__':
    main()


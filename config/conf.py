"""
----------------------------------
@Time: 2019/11/04
@Author: Tian
@Files: conf.py
@IDE: Pycharm
----------------------------------
"""

from datetime import datetime
import os

#项目根目录
projectDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#报告目录
reportDir = os.path.join(projectDir, 'report')
#ui 对象库config.ini文件所在目录
configDir = os.path.join(projectDir, 'config', 'config.ini')
#测试数据所在目录
excelPath = os.path.join(projectDir, 'data', 'tcData.xlsx')
#当前时间
currentTime = datetime.now().strftime('%H_%M_%S')
#端口
port = '25'

#邮件配置信息
#邮件服务器
smtpServer = 'smtp.126.com'
#发送者
fromUser = 'autotestsst@126.com'
#发送者密码
fromPassWord = 'Dublin14'
#接收者
toUser = 'tmaostats1@163.com'
#邮件标题
subject  = '项目自动化测试报告'
#邮件正文
contents = '测试报告正文'
#报告名称
htmlName = r'{}\testReport{}.html'.format(reportDir, currentTime)


#脚本执行命令
args = r'pytest --html=' + htmlName+ ' ' + '--self-contained-html'
args_login = r'pytest --html='+ htmlName+ ' ' + '-m' + ' ' + 'loginTest'+ ' --self-contained-html'
args_contact = r'pytest --html='+ htmlName+ ' ' + '-m' + ' ' + 'contactTest'+ ' --self-contained-html'
args_sendmail = r'pytest --html='+ htmlName+ ' ' + '-m' + ' ' + 'sendMailTest'+ ' --self-contained-html'

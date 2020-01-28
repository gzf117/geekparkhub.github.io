# -*- coding:utf-8 -*-
# 
# Geek International Park | 极客国际公园
# GeekParkHub | 极客实验室
# Website | https://www.geekparkhub.com
# Description | Open · Creation | 
# Open Source Open Achievement Dream, GeekParkHub Co-construction has never been seen before.
# HackerParkHub | 黑客公园
# Website | https://www.hackerparkhub.org
# Description | In the spirit of fearless exploration, create unknown technology and worship of technology.
# GeekDeveloper : JEEP-711
# 
# @Author : system
# @Version : 0.2.5
# @Program : 邮件 | mail
# @File : 17_mail.py
# @Description : Python 进阶篇 - 邮件 | Advanced Python - Mail

# 导入模块 | Import module
from email import encoders as ed
from email.header import Header as hd
from email.mime.text import MIMEText as mt
from email.utils import parseaddr as pa, formataddr as fa
import smtplib as st
from email.parser import Parser as ps
from email.header import decode_header as dh
import poplib as pl


# 定义 格式化地址 函数 | Definition format address function
def _format_addr(s):
    name, addr = pa(s)
    return fa((hd(name, 'UTF-8').encode(), addr))


# 定义 发送邮件 函数 | Define send mail function
def send_function():
    from_addr = input('From: \n')  # 输入Email地址 | Enter email address
    password = input('Password: \n')  # 输入Email地址口令 | Enter email address and password
    to_addr = input('To: \n')  # 输入收件人地址 | Enter recipient address
    smtp_server = input('SMTP server: \n')  # 输入SMTP服务器地址 | Enter SMTP server address

    '''
    构造MIMEText对象
    参数说明: 
                `Hello, Send by Python...` 表示邮件正文
                `plain` 表示邮件类型为纯文本
                `UTF-8` 表示邮件编码
    '''
    message = mt('Hello, Send by Python...', 'plain', 'UTF-8')
    message['From'] = _format_addr('Dev <%s>' % from_addr)
    message['To'] = _format_addr('Administrator <%s>' % to_addr)
    message['Subject'] = hd('Greetings from SMTP……', 'UTF-8').encode()

    server = st.SMTP(smtp_server, 25)  # 定义 SMTP协议默认端口 | Define the SMTP protocol default port
    server.set_debuglevel(1)  # 打印SMTP服务器交互信息 | Print SMTP server interaction information
    server.login(from_addr, password)  # 登录SMTP服务器 | Log in to the SMTP server
    server.sendmail(from_addr, [to_addr], message.as_string())  # 发送邮件 | send email
    server.quit()  # 退出SMTP服务器 | Exit SMTP server


# 定义 收取邮件 函数 | Define receive mail function
def receive_mail():
    # 输入邮件地址&口令&POP3服务器地址 | Enter email address & password & POP 3 server address
    email = input('Email: ')
    password = input('Password: ')
    pop3_server = input('POP3 server: ')
    # 连接到POP3服务器:
    server = pl.POP3(pop3_server)
    # 可以打开或关闭调试信息:
    server.set_debuglevel(1)
    # 可选:打印POP3服务器的欢迎文字:
    print(server.getwelcome().decode('utf-8'))
    # 身份认证:
    server.user(email)
    server.pass_(password)
    # stat()返回邮件数量和占用空间:
    print('Messages: %s. Size: %s' % server.stat())
    # list()返回所有邮件的编号:
    resp, mails, octets = server.list()
    # 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
    print(mails)
    # 获取最新一封邮件, 注意索引号从1开始:
    index = len(mails)
    resp, lines, octets = server.retr(index)
    # lines存储了邮件的原始文本的每一行,
    # 可以获得整个邮件的原始文本:
    msg_content = b'\r\n'.join(lines).decode('UTF-8')
    # 稍后解析出邮件:
    msg = ps().parsestr(msg_content)
    print_info(msg)
    # 可以根据邮件索引号直接从服务器删除邮件:
    # server.dele(index)
    # 关闭连接:
    server.quit()


# 定义 查找字符集 函数 | Definition Find Character Set Function
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


# 定义 解码字符集 函数 | Definition decode character set function
def decode_str(s):
    value, charset = dh(s)[0]
    if charset:
        value = value.decode(charset)
    return value


# 定义 打印信息 函数 | Definition print information function
def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = pa(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))


# 调用 函数 | call function
send_function()
receive_mail()

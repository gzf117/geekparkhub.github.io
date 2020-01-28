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
# @Program : TCP 网络编程 | TCP network programming
# @File : tcp_socket.py
# @Description :  Python 进阶篇 - 网络编程 | Advanced Python-Network Programming

# 导入模块 | Import module
import socket as sk


# 定义 函数 | Defining functions
def socket_function():
    # 创建 Socket | Create Socket
    '''
    参数说明 :
                `AF_INET6` 指定IPv6网络协议
                `SOCK_STREAM` 指定面向流TCP协议
    '''
    s = sk.socket(sk.AF_INET6, sk.SOCK_STREAM)

    # 创建 连接 | Create connection
    '''
    定义 服务器IP地址&端口号
    '''
    s.connect(('58.49.227.129', 80))

    # 发送 数据 | send data
    '''
    向服务端发送请求
    '''
    s.send(b'GET / HTTP/1.1\r\nHost: 58.49.227.129\r\nConnection: close\r\n\r\n')

    # 接收 数据 | Receive data
    buffer = []
    while True:
        byte_size = s.recv(1024)
        if byte_size:
            buffer.append(byte_size)
        else:
            break
    data = b' '.join(buffer)

    # 关闭资源 | Close resource
    s.close()

    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('UTF-8'))

    # 数据写入文件
    with open('test.html', 'wb') as f:
        f.write(html)

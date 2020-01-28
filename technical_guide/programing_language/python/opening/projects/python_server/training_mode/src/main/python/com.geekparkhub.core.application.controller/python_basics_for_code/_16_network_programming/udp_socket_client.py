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
# @Program : UDP 网络编程 | UDP network programming
# @File : udp_socket_client.py
# @Description : Python 进阶篇 - 网络编程 | Advanced Python-Network Programming

# 导入模块 | Import module
import socket as sk


# 定义 客户端 函数 | Defining Client functions
def udp_client():
    # 创建 Socket | Create Socket
    '''
    参数说明 :
                `AF_INET` 指定IPv4网络协议
                `SOCK_STREAM` 指定面向流TCP协议
    '''
    s = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

    lists = [b'Edward', b'System', b'Juliet', b'Romeo']

    for x in lists:
        # 发送数据 | send data
        s.sendto(x, ('127.0.0.1', 9999))
        # 接收数据 | Receive data
        print(s.recv(1024).decode('UTF-8'))
    # 关闭资源 | Close resource
    s.close()


# 调用 函数 | call function
udp_client()

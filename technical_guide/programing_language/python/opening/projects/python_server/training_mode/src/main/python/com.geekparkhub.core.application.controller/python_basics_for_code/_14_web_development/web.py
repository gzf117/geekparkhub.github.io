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
# @Program : Web开发 | Web development
# @File : web.py
# @Description : Python 进阶篇 - Web开发 | Advanced Python - Web Development

# WSGI 接口 | WSGI interface

# 定义 HTTP处理函数 | Define HTTP handler function
'''
参数说明:
            `env` 包含所有HTTP请求信息的字典对象
            `start_response` 发送HTTP响应的函数
'''


def wsgi_function(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello %s !</h1>' % (env['PATH_INFO'][1:] or 'web')
    return [body.encode('UTF-8')]

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
# @File : __init__.py.py
# @Description : Python 进阶篇 - Web开发 | Advanced Python - Web Development

# 导入模块 | Import module
from wsgiref.simple_server import make_server as mk
from _14_web_development.web import wsgi_function as wd

# 定义 主模块 | Definition Main module
if __name__ == '__main__':
    # 启动WSGI服务器 | Start the WSGI server
    httpd = mk('', 9800, wd)
    print('Serving HTTP on port 9800...')
    httpd.serve_forever()

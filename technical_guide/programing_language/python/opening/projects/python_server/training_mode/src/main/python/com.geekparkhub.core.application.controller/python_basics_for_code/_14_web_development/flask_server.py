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
# @Program : flask_server
# @File : flask_server.py
# @Description : Python 进阶篇 - Web开发 | Advanced Python - Web Development

# 导入模块 | Import module
from flask import Flask
from flask import request as req

# 初始化 | initialization
service = Flask(__name__)
'''
请求类型 & 处理响应说明: 
    请求类型：GET请求 | 处理响应：'/'  返回Home首页
    请求类型：GET请求 | 处理响应：`/signin` 返回登录页, 显示登录表单
    请求类型：POST | 处理响应：`/signin` 处理登录表单，显示登录结果
'''


# 定义 处理Home路由 | Define Handle Home routing
@service.route('/', methods=['GET', 'POST'])
# 定义 处理响应函数 | Definition Processing Response Function
def home():
    return '''
    <h1>Welcome to Home</h1> 
    <p><a href="/signin">Sign In</a></p>
    '''


# 定义 处理登录路由 | Definition Handle Login Route
@service.route('/signin', methods=['GET'])
# 定义 处理响应函数 | Definition Processing Response Function
def signin_form():
    return '''
    <form action="/signin" method="post">
    <p><input name="UserName"/></p>
    <p><input name="PassWord" type="password"/></p>
    <p><a href="/">Return Home</a></p>
    <p><button type="submit">Sign In</button></p>
    </form>
    '''


# 定义 登录路由 | Define login routes
@service.route('/signin', methods=['POST'])
# 定义 处理响应函数 | Definition Processing Response Function
def signin():
    # 验证登录信息 | Verify login information
    if req.form['UserName'] == 'Admin' and req.form['PassWord'] == 'password':
        return '''
        <h3>Hello Admin!</h3> <p><a href="/">Return Home</a></p>
        '''
    return '<h3>Bad UserName or PassWord.</h3>'


# 定义 主模块 | Definition Main module
if __name__ == '__main__':
    # 启动运行服务 | Start running service
    service.run()

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
# @Program : 异步I/O | Asynchronous I / O
# @File : 22_asynchronous_io.py
# @Description : Python 进阶篇 - 异步I/O | Advanced Python - Asynchronous I / O

# 导入模块 | Import module
import threading as tg
import asyncio as ao
from aiohttp import web as wb


# 定义 异步IO 类 | Define AsynchronousReadWrite class
class AsynchronousReadWrite:
    '''
    协程生产者&消费者执行流程：子程序就是协程的一种特例
        `coroutine_consumer()`方法是生成器(generator), 将coroutine_consumer传入`coroutine_producer()`方法
        1. 首先调用`parameter.send(None)`启动生成器.
        2. 然后一旦生产消息, 通过`parameter.send(n)`切换到`coroutine_consumer`执行.
        3. `coroutine_consumer`通过`yield`拿到消息, 处理又通过`yield`把结果回传.
        4. `coroutine_producer()`拿到`coroutine_consumer`处理结果, 继续生产下一条消息.
        5. `coroutine_producer决定不生产了, 是通过`parameter.close()`关闭`coroutine_consumer`整个过程结束.
        整个流程无锁, 由一个线程执行, `produce`和`consumer`协作完成任务, 所以称为“协程”, 而非线程的抢占式多任务
    '''

    # 定义 协程 消费者 方法 | Definition coroutine consumer method
    def coroutine_consumer(self):
        r = ' '
        while True:
            n = yield r
            if not n:
                return
            print('[CONSUMER] Consuming %s...' % n)
            r = '200 OK'

    # 定义 协程 生产者 方法 | Definition coroutine producer method
    def coroutine_producer(self, parameter):
        parameter.send(None)
        n = 0
        while n < 5:
            n = n + 1
            print('[PRODUCER] Producing %s...' % n)
            r = parameter.send(n)
            print('[PRODUCER] Consumer Return: %s' % r)
        parameter.close()

    # 定义 asyncio 异步IO方法 | Define asyncio asynchronous IO method
    '''
    Python 3.5以下使用`asyncio.@coroutine`装饰器 修饰生成器为coroutine类型
    Python 3.8起已弃用`@coroutine`装饰器, 改用`async def`修饰coroutine类型
    '''

    async def asynchronous_method(self, nums):
        print('Hello World! (%s)' % tg.currentThread())
        '''
        Python 3.5以下使用 `yield from asyncio.sleep(nums)`调用异步睡眠
        '''
        # 异步调用睡眠
        await ao.sleep(nums)
        print('Hello Again! (%s)' % tg.currentThread())

    # 定义 执行 协程异步IO 方法 | Define execute coroutine asynchronous IO method
    def run_asyncio(self, func):
        # 定义 获取循环事件 | Definition Get loop event
        loop = ao.get_event_loop()
        # 定义 执行 协程 | Definition execution coroutine
        tasks = [func, func]
        loop.run_until_complete(ao.wait(tasks))
        # 关闭事件 | Close event
        loop.close()

    # 定义 异步获取网站服务状态 方法 | Define Get website service status asynchronously
    async def get_website_status(self, host):
        print('Ge WebSite  %s...' % host, '\n')
        connect = ao.open_connection(host, 80)
        reader, writer = await connect
        header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
        writer.write(header.encode('UTF-8'))
        await writer.drain()
        while True:
            line = await reader.readline()
            if line == b'\r\n':
                break
            print('%s Header => %s' % (host, line.decode('UTF-8').rstrip()))
        # 关闭流 | Close stream
        writer.close()

    # 运行 异步获取网站服务状态 方法 | Run asynchronously to get website service status method
    def run_get_website(self, url):
        # 定义 获取循环事件 | Definition Get loop event
        loop = ao.get_event_loop()
        # 定义 执行 协程 | Definition execution coroutine
        tasks = [self.get_website_status(x) for x in url]
        loop.run_until_complete(ao.wait(tasks))
        # 关闭事件 | Close event
        loop.close()


'''
异步Web应用程序 | Async Web Application
定义 简易HTTP服务器 方法 | Define a simple HTTP server method
'''
# 定义 路由器 | Definition router
routes = wb.RouteTableDef()


# 定义 Web应用 首页 方法 | Defining a Web Application Home Method
@routes.get('/')
async def home(request):
    await ao.sleep(0.5)
    return wb.Response(body=b'<h1>Welcome To Home!</h1>', headers={'content-type': 'text/html'})


# 定义 Web应用 JSON 方法 | Define web application JSON method
@routes.get('/json/{name}')
async def json_method(request):
    await ao.sleep(0.1)
    return wb.json_response({'name': request.match_info['name'] or 'index'})


# 定义 Web应用 主页 方法 | Define Web Application Home Method
@routes.get('/mains/{name}')
async def mains(request):
    await ao.sleep(0.5)
    return wb.Response(body="<h1>Hello %s</h1>" % request.match_info['name'], headers={'content-type': 'text/html'})


# 定义 Web应用 初始化 方法 | Define web application initialization method
async def init():
    # 初始化服务 | Initialize the service
    app_server = wb.Application()
    app_server.add_routes(routes)
    # 运行HTTP服务 | Run HTTP service
    runner = wb.AppRunner(app_server)
    await runner.setup()
    website = wb.TCPSite(runner, '127.0.0.1', 8000)
    await website.start()
    print('======== Running on http://127.0.0.1:8000 ========')


# 定义 主模块 | Definition Main module
if __name__ == '__main__':
    # 创建 实例 | Create instance
    a = AsynchronousReadWrite()
    # 调用 方法 | Call method
    consumer = a.coroutine_consumer()
    a.coroutine_producer(consumer)
    coroutine_method = a.asynchronous_method(3)
    a.run_asyncio(coroutine_method)
    HOST = ['www.youtube.com', 'www.google.com', 'www.163.com', 'www.github.com', 'www.python.org']
    a.run_get_website(HOST)
    init()

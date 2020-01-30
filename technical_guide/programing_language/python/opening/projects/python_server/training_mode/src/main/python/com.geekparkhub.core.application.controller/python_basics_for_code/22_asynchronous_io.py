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


# 定义 主模块 | Definition Main module
if __name__ == '__main__':
    # 创建 实例 | Create instance
    a = AsynchronousReadWrite()
    # 调用 方法 | Call method
    consumer = a.coroutine_consumer()
    a.coroutine_producer(consumer)

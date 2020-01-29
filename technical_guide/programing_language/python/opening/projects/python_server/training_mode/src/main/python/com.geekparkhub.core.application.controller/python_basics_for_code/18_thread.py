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
# @Program : 线程 | Thread
# @File : 18_thread.py
# @Description : Python 进阶篇 - 线程 | Advanced Python - Threads

# 导入模块 | Import module
import os as o, time as te, random as rm, threading as tg
from multiprocessing import Process as pes, Pool as pl, Queue as qu
import subprocess as sp


# 定义 子进程 函数 | Definition Child process function
def child_process_function():
    print('Process (%s) start...' % o.getpid())
    # Only works on Unix/Linux/Mac:
    pid = o.fork()
    if pid == 0:
        print('I am child process (%s) and my parent is %s.' % (o.getegid(), o.getppid()))
    else:
        print('I (%s) just created a child process (%s).' % (o.getpid(), pid))


# 定义 运行过程 函数 | Definition run function
def run_proc(name):
    print('Run child process %s (%s)...' % (name, o.getpid()))


# 定义 父进程 函数 | Definition parent process function
def parent_process_function():
    print('Parent process %s.' % o.getpid())
    p = pes(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()  # 启动
    p.join()  # 等待子进程结束后再继续往下运行, 通常用于进程间的同步
    print('Child process end.')


# 定义 进程池 函数 | Define process pool function
def long_time_task(name):
    print('Run task %s (%s)...' % (name, o.getpid()))
    start = te.time()
    te.sleep(rm.random() * 3)
    end = te.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


# 定义 子进程 函数 | Definition child process function
def run_task():
    print('Parent process %s.' % o.getpid())
    p = pl(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


# 定义 子进程 函数 | Definition child process function
def child_process():
    print('$ nslookup www.python.org')
    r = sp.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)

    print('$ nslookup')
    p = sp.Popen(['nslookup'], stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('UTF-8'))
    print('Exit code:', p.returncode)


# 进程通信 | Process communication
# 定义 写数据进程 函数 | Definition data write function
def write_function(queue):
    print('Process to write: %s' % o.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        queue.put(value)
        te.sleep(rm.random())


# 定义 读数据进程 函数 | Definition data read function
def read_function(queue):
    print('Process to read: %s' % o.getpid())
    while True:
        value = queue.get(True)
        print('Get %s from queue.' % value)


# 定义 父进程队列 函数 | Define the parent process Queue function
def parent_process_queue():
    # 父进程创建Queue, 并传给各个子进程
    q = qu()
    pw = pes(target=write_function, args=(q,))
    pr = pes(target=read_function, args=(q,))
    # 启动子进程pw写入
    pw.start()
    # 启动子进程pr读取
    pr.start()
    # 等待pw结束
    pw.join()
    # pr进程里是死循环, 无法等待其结束, 只能强行终止:
    pr.terminate()


# 多线程 | Multithreading
# 定义 函数 | Definition function
def loops():
    print('Thread %s is Running...' % tg.current_thread().name)
    x = 0
    while x < 5:
        x = x + 1
        print('Thread %s >>> %s' % (tg.current_thread().name, x))
        te.sleep(1)
    print('Thread %s Ended.' % tg.current_thread().name)


# 执行 多线程 函数 | Execute multithreaded function
def run_loop():
    print('Thread %s is Running...' % tg.current_thread().name)
    t = tg.Thread(target=loops, name='LoopThread')
    t.start()
    t.join()
    print('Thread %s Ended.' % tg.current_thread().name)


# 定义 本地线程 函数 | Define local thread function
local_school = tg.local()


def process_student():
    # 获取当前线程关联的student
    std = local_school.student
    print('Hello, %s (in %s)' % (std, tg.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student
    local_school.student = name
    process_student()


def run_native_thread():
    t1 = tg.Thread(target=process_thread, args=('SYSTEM',), name='Thread-A')
    t2 = tg.Thread(target=process_thread, args=('BOUUS',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()


# 导入模块 | Import module
import random as rd, time as t, queue as q, sys as s
from multiprocessing.managers import BaseManager as bm

# 定义 发送任务队列 | Definition send task queue
task_queue = q.Queue()
# 定义 接收结果队列 | Definition receive result queue
result_queue = q.Queue()


# 定义 任务Master 类 | Definition Task Master Class
class TaskMaster(bm):

    # 定义 运行任务 方法 | Define Run Task Method
    def run_task(self):
        # 将两个Queue注册到网络, callable参数关联Queue对象
        TaskMaster.register('get_task_queue', callable=lambda: task_queue)
        TaskMaster.register('get_result_queue', callable=lambda: result_queue)
        # 绑定5000端口, 设置验证码'abc'
        manager = TaskMaster(address=('', 5000), authkey=b'abc')
        # 启动Queue
        manager.start()
        # 获得通过网络访问的Queue对象
        task = manager.get_task_queue()
        result = manager.get_result_queue()
        # 追加任务
        for i in range(10):
            n = rd.randint(0, 10000)
            print('Put task %d...' % n)
            task.put(n)
        # 从result队列读取结果
        print('Try get results...')
        for i in range(10):
            r = result.get(timeout=10)
            print('Result: %s' % r)
        # 关闭任务
        manager.shutdown()
        print('master exit.')


# 定义 任务Worker 类 | Definition Task Worker Class
class TaskWorker(bm):

    # 定义 运行任务 方法 | Define Run Task Method
    def run_task(self):
        # 由于TaskWorker通过网络获取Queue, 注册时提供队列名称
        TaskWorker.register('get_task_queue')
        TaskWorker.register('get_result_queue')

        # 连接到服务器, 也就是运行TaskMaster机器
        server_addr = '127.0.0.1'
        print('Connect to server %s...' % server_addr)
        # 端口和验证码注意保持与TaskMaster设置完全一致
        m = TaskWorker(address=(server_addr, 5000), authkey=b'abc')
        # 网络连接
        m.connect()
        # 获取Queue对象
        task = m.get_task_queue()
        result = m.get_result_queue()
        # 从task队列取任务, 并把结果写入result队列
        for i in range(10):
            try:
                n = task.get(timeout=1)
                print('run task %d * %d...' % (n, n))
                r = '%d * %d = %d' % (n, n, n * n)
                t.sleep(1)
                result.put(r)
            except q.Empty:
                print('task queue is empty.')
        # 处理结束
        print('worker exit.')


# 定义 主模块 | Definition Main module
if __name__ == '__main__':
    # 调用 函数 | call function
    child_process_function()
    parent_process_function()
    run_task()
    child_process()
    parent_process_function()
    run_loop()
    run_native_thread()
    # 创建实例 | Create instance
    tm = TaskMaster()
    tw = TaskWorker()
    # 调用 方法 | Call method
    tm.run_task()
    tw.run_task()

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
import os as o, time as te, random as rm
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


# 定义 主模块 | Definition Main module
if __name__ == '__main__':
    # 调用 函数 | call function
    child_process_function()
    parent_process_function()
    run_task()
    child_process()
    parent_process_function()

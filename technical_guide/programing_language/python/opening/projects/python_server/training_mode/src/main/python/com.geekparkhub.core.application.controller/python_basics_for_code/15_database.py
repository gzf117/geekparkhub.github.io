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
# @Program : 数据库 | database
# @File : 15_database.py
# @Description : Python 进阶篇 - 数据库 | Advanced Python-Database

# 导入模块 | Import module
import sqlite3 as sl
import os as o


# 数据库 for SQLite | Database for SQLite

# 定义 函数 | Defining functions
def database_for_sqlite_insert():
    '''
    连接到SQLite数据库, 数据库文件是test.db
    如果文件不存在则自动在当前目录创建
    '''
    connection = sl.connect('test.db')

    # 创建 Cursor | Create Cursor
    cursor = connection.cursor()

    # 创建 数据表 | Create data table
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

    # 创建 插入语句 | Create insert statement
    cursor.execute('insert into user (id, name) values (\'1\', \'system\')')

    # 通过rowcount获得插入的行数 | Get the number of inserted rows by rowcount
    print('rowcount=', cursor.rowcount)

    # 关闭Cursor | Close Cursor
    cursor.close()

    # 提交事务 | Commit transaction
    connection.commit()

    # 关闭资源 | Close resource
    connection.close()


def database_for_sqlite_select():
    '''
    连接到SQLite数据库, 数据库文件是test.db
    如果文件不存在则自动在当前目录创建
    '''

    connection = sl.connect('test.db')

    # 创建 Cursor | Create Cursor
    cursor = connection.cursor()

    # 执行查询语句 | Execute query
    cursor.execute('select * from user where id=?', '1')

    # 获得查询结果集 | Get query result set
    values = cursor.fetchall()
    print('values=', values)

    # 关闭Cursor | Close Cursor
    cursor.close()

    # 关闭资源 | Close resource
    connection.close()


# 定义 类 | Definition class
class Student:
    # 定义 初始化 方法 | Define initialization method
    def __init__(self):
        db_file = o.path.join(o.path.dirname(__file__), 'student_test.db')
        if o.path.isfile(db_file):
            o.remove(db_file)
        # 创建 连接 | Create connection
        conn = sl.connect(db_file)
        # 创建 Cursor | Create Cursor
        cursor = conn.cursor()
        cursor.execute('create table student(id varchar(20) primary key, name varchar(20), score int)')
        cursor.execute(r"insert into student values ('A-001', 'Adam', 95)")
        cursor.execute(r"insert into student values ('A-002', 'Bart', 62)")
        cursor.execute(r"insert into student values ('A-003', 'Lisa', 78)")
        cursor.close()
        conn.commit()
        conn.close()

    # 定义 方法 | 返回指定分数区间的姓名, 按分数从低到高排序
    def get_score_in(self, low, high):
        global cursor, connection
        try:
            connection = sl.connect('student_test.db')
            cursor = connection.cursor()
            cursor.execute('select name from student where score >=? and score <=? order by score', (low, high))
            values = cursor.fetchall()
            return list(map(lambda v: v[0], values))
        except BaseException as e:
            print('Connection Error!', e)
        finally:
            cursor.close()
            connection.close()


# 数据库 for MySQL | Database for MySQL
# 定义 函数 | Defining functions
def database_for_mysql():
    pass


# 数据库 for SQL Alchemy | Database for SQL Alchemy
# 定义 函数 | Defining functions
def database_for_sqlalchemy():
    pass


# 定义 主模块 | Definition Main module
if __name__ == '__main__':
    # 调用 函数 | call function
    # database_for_sqlite_insert()
    # database_for_sqlite_select()
    s = Student()
    s.__init__()
    print('score: 80~95=', s.get_score_in(80, 95))
    print('score: 60~80=', s.get_score_in(60, 80))
    print('score: 60~100=', s.get_score_in(60, 100))

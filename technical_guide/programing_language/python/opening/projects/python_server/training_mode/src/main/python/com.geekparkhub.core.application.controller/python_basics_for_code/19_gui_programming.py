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
# @Program : GUI 编程 | GUI programming
# @File : 19_gui_programming.py
# @Description : Python 进阶篇 - GUI 编程 | Advanced Python - GUI Programming

# 导入模块 | Import module
from tkinter import *
import tkinter.messagebox as mb
import turtle as te


# 定义 GUI应用 类 | Define the GUI application class
class GUIApplication(Frame):

    # 定义 初始化 方法 | Define initialization method
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()  # 调用 简单布局方法 | Call simple layout method
        self.create_widgets()  # 调用 创建组件方法 | Call the create component method

    # 定义 创建组件 方法 | Definition create component method
    def create_widgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.text_method)
        self.alertButton.pack()

    # 定义 文本输出 方法 | Define text output method
    def text_method(self):
        name = self.nameInput.get() or 'World'
        mb.showinfo('Message Info', 'Hello, %s' % name)


# 定义 绘制长方形图形 函数 | Definition draw rectangle function
def drawing_rectangle_function(turtles):
    # 定义 笔刷宽度 | Definition brush width
    turtles.width(4)

    # 定义 前进 | Definition go ahead
    turtles.forward(200)
    # 定义 右转90度 | Definition 90 degrees right
    turtles.right(90)

    # 定义 笔刷颜色 | Definition brush color
    turtles.pencolor('blue')
    turtles.forward(100)
    turtles.right(90)

    turtles.pencolor('green')
    turtles.forward(200)
    turtles.right(90)

    turtles.pencolor('red')
    turtles.forward(100)
    turtles.right(90)

    # 定义 关闭窗口 | Definition Close window
    turtles.done()


# 定义 绘制五角星图形 函数 | Definition draw five-pointed star function
def drawing_five_pointed_function(turtles, num_x, num_y):
    turtles.pu()
    turtles.goto(num_x, num_y)
    turtles.pd()
    turtles.seth(0)
    for i in range(5):
        turtles.fd(40)
        turtles.rt(144)


def run_drawing_five_pointed_function(turtles):
    for x in range(0, 250, 50):
        drawing_five_pointed_function(turtles, x, 0)
    turtles.done()


# 定义 绘制 分型树图形 函数 | Definition draw fractal tree graph function

# 定义颜色数值 | Define color values
te.colormode(255)

te.lt(90)

# 定义全局变量 | Defining global variables
lv = 14
le = 120
s = 45

# 定义宽度 | Define width
te.width(lv)

r = 0
g = 0
b = 0
te.pencolor(r, g, b)

te.penup()
te.bk(le)
te.pendown()
te.fd(le)


def drawing_fractal_tree_graph_function(turtles, l, level):
    global r, g, b
    # save the current pen width
    w = turtles.width()

    # narrow the pen width
    turtles.width(w * 3.0 / 4.0)
    # set color:
    r = r + 1
    g = g + 2
    b = b + 3
    turtles.pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l

    turtles.lt(s)
    turtles.fd(l)

    if level < lv:
        drawing_fractal_tree_graph_function(turtles, l, level + 1)
    turtles.bk(l)
    turtles.rt(2 * s)
    turtles.fd(l)

    if level < lv:
        drawing_fractal_tree_graph_function(turtles, l, level + 1)
    turtles.bk(l)
    turtles.lt(s)

    # restore the previous pen width
    turtles.width(w)


te.speed("fastest")
drawing_fractal_tree_graph_function(te, le, 4)
te.done()

# 定义 主模块 | Definition Main module
if __name__ == '__main__':
    # 创建实例 | Create instance
    g1 = GUIApplication()
    # 调用 方法 | Call method
    g1.master.title('Application')  # 设置窗口标题信息 | Set window title information
    g1.mainloop()
    # 调用 函数 | call function
    drawing_rectangle_function(te)
    run_drawing_five_pointed_function(te)

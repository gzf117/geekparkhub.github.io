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
# @Program : JSON 编码 解码 | # @Program : JSON 编码 解码 |
# @File : 21_json_parsing.py
# @Description : Python 进阶篇 - JSON 编码 解码 | Advanced Python - JSON encoding and decoding

# 导入模块 | Import module
import json as jn
import demjson as dj

'''
定义数组, 将数组编码为JSON格式数据
Define an array, encode the array into JSON format data
'''
array_data = [{'name': 'Juliet', 'age': 18, 'gender': 'girl', 'Hobby': 'music', 'constellation': 'Libra'}]

'''
定义JSON, 解码JSON返回Python数据类型
Define JSON, decode JSON and return Python data type
'''
json_data = '{"name":"Juliet","age":18,"gender":"girl","Hobby":"music","constellation":"Libra"}'


# 定义 数组转换JSON 函数 | Definition array conversion JSON function
def array_conversion_json(values):
    '''
    数据格式化输出 | Data formatted output
    参数说明 | Parameter Description:
        `values` 表示加载元数据
        `sort_keys` 表示key排序选项, False返回升序, True返回降序
        `indent` 表示缩进长度
        `separators` 表示分隔符
    :param values:
    :return:
    '''
    j = jn.dumps(values, sort_keys=False, indent=1, separators=(',', ': '))
    print('ArrayData to JsonData=', j)


# 定义 JSON 转换为Python数据类型 函数 | Define JSON to Python data type function
def json_conversion_data(values):
    text = jn.loads(values)
    print('JSON to Python data type=', text)


# 定义 数组转换JSON 函数 | Definition array conversion JSON function
def array_coding_json(values):
    j = dj.encode(values)
    print('ArrayData to JsonData=', j)


# 定义 JSON 转换为Python数据类型 函数 | Define JSON to Python data type function
def json_coding_data(values):
    text = dj.decode(values)
    print('JSON to Python data type=', text)


# 定义 主模块 | Definition Main module
if __name__ == '__main__':
    # 调用函数 | call function
    array_conversion_json(array_data)
    json_conversion_data(json_data)
    array_coding_json(array_data)
    json_coding_data(json_data)

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
# @Program : XML 解析 | XML Parsing
# @File : 20_xml_parsing.py
# @Description : Python 进阶篇 - XML 解析 | Advanced Python - XML Parsing

# 导入模块 | Import module
import xml.sax
from xml.dom.minidom import parse as pe
import xml.dom.minidom as mm


# 定义 xml解析类 | Definition xml parsing class
class XmlParsing(xml.sax.ContentHandler):

    # 定义 初始化方法 | Definition initialization method
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""
        super().__init__()

    # 定义 SAX解析XML 方法 | Define SAX parsing XML method
    # 元素开始事件处理 | Element start event processing
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            print('**********Movie**********')
            title = attributes["title"]
            print('Title:', title)

    # 元素结束事件处理 | Element end event processing
    def endElement(self, tag):
        if self.CurrentData == "type":
            print('Type:', self.type)
        elif self.CurrentData == "format":
            print('Format:', self.format)
        elif self.CurrentData == "year":
            print('Year:', self.year)
        elif self.CurrentData == "rating":
            print('Rating:', self.rating)
        elif self.CurrentData == "stars":
            print('Stars:', self.stars)
        elif self.CurrentData == "description":
            print('Description:', self.description, '\n')
        self.CurrentData = ""

    # 内容事件处理 | Content event processing
    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content

    # 定义 DOM解析XML 方法 | Define DOM parsing XML method
    def dom_parsing_xml_method(self, path):
        # 加载数据 | Load Data
        dom_tree = pe(path)
        # 采集元素 | Collecting elements
        collection = dom_tree.documentElement
        # 条件判断 | Condition judgment
        if collection.hasAttribute("shelf"):
            print('Root element : %s ' % collection.getAttribute("shelf"))
        # 在集合中获取所有数据 | Get all data in a collection
        movies = collection.getElementsByTagName("movie")
        # 打印数据详细信息 | Print data details
        for data_info in movies:
            print('**********Movie**********')
            if data_info.hasAttribute("title"):
                print('Title: %s' % data_info.getAttribute("title"))
            types = data_info.getElementsByTagName('type')[0]
            print('Type: %s' % types.childNodes[0].data)
            formats = data_info.getElementsByTagName('format')[0]
            print('Format: %s' % formats.childNodes[0].data)
            rating = data_info.getElementsByTagName('rating')[0]
            print('Rating: %s' % rating.childNodes[0].data)
            description = data_info.getElementsByTagName('description')[0]
            print('Description: %s' % description.childNodes[0].data, '\n')


# 定义 主模块 | Definition Main module
if __name__ == '__main__':
    # 定义文件路径 | Define file path
    FILE_PATHS = '../resources/xml_file/movies.xml'
    # 创建 XMLReader | Create XMLReader
    parser = xml.sax.make_parser()
    # 关闭命名空间 | turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    # 创建实例 | Create instance
    x = XmlParsing()
    parser.setContentHandler(x)
    # 装载数据进行解析 | Load data for parsing
    parser.parse(FILE_PATHS)
    # 调用方法 | Calling method
    x.dom_parsing_xml_method(FILE_PATHS)

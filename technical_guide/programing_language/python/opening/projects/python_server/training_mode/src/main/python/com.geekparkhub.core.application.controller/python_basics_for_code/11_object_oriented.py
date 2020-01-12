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
# @Program : 面向对象 | Object-oriented
# @File : 11_object_oriented.py
# @Description : Python 基础篇 - 面向对象 | Python Basics-Object Oriented

# 定义 实例 | Definition instance
# 创建int实例 | Create an int instance
nums = int(100)
print('nums=', nums, type(nums))


# 定义 类 | Definition class
class CoreClass:
    pass


# 创建对象实例 | Create Object instance
cc = CoreClass()
cc1 = CoreClass()
cc2 = CoreClass()
cc3 = CoreClass()
print('cc=', cc, type(cc))

# 检查对象实例 | Check object instance
res1 = isinstance(cc, CoreClass)
res2 = isinstance(cc1, CoreClass)
res3 = isinstance(cc2, CoreClass)
res4 = isinstance(cc2, int)
print('res1=', res1)
print('res2=', res2)
print('res3=', res3)
print('res4=', res4)


# 定义 类 | Definition class
class Product():
    # 定义 属性 | Definition attribute
    product_name = 'Mobile phone'
    product_size = '26 * 30'
    product_weight = 20
    product_colour = 'black'

    # 定义 方法 | Definition method
    def product_info(self):
        print('product_info=', self.product_name, self.product_size, self.product_weight, self.product_colour)


# 创建实例 | Create instance
p1 = Product()
p2 = Product()

# 调用 属性 | Call attribute
r1 = p1.product_name = 'Apple Mobile phone'
r2 = p2.product_colour = 'Gradient color'
print('product_name=', r1)
print('product_colour=', r2)

# 调用 方法 | Call method
p1.product_info()
p2.product_info()


# 对象 初始化 | Object initialization
# 定义 类 | Definition class
class Commodity:
    # 定义初始化方法 | Define the initialization method
    def __init__(self, commodity_brand, commodity_model, commodity_colour, commodity_operating_system, commodity_ram,
                 commodity_of_sale, commodity_price):
        self.commodity_brand = commodity_brand
        self.commodity_model = commodity_model
        self.commodity_colour = commodity_colour
        self.commodity_operating_system = commodity_operating_system
        self.commodity_ram = commodity_ram
        self.commodity_of_sale = commodity_of_sale
        self.commodity_price = commodity_price

    # 定义 自定义 方法 | Define custom method
    def commodity_info(self):
        print('Commodity Info:', self.commodity_brand,
              self.commodity_model, self.commodity_colour, self.commodity_operating_system, self.commodity_ram,
              self.commodity_of_sale, self.commodity_price)


# 创建实例 | Create instance
commodity_1 = Commodity('Apple', 'iphone X', 'White', 'Ios', '256GB', 'Global', '4500RMB')
commodity_2 = Commodity('Samsung', 'S3', 'Blue', 'Android', '16GB', 'Global', '900RMB')
commodity_3 = Commodity('Huawei', 'P30', 'Black', 'Android', '256GB', 'Global', '5600RMB')

# 调用 方法 | Call method
commodity_1.commodity_info()
commodity_2.commodity_info()
commodity_3.commodity_info()

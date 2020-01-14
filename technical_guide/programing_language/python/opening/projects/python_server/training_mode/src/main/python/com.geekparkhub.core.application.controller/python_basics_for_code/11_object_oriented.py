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


# 面向对象 (封装) | Object-oriented (encapsulation)
# 定义 类 | Definition class
class Animals:

    # 定义 初始化方法 | Definition initialization method
    def __int__(self, animal_name, animal_type, animal_age, animal_diet):
        self.hidden_animal_name = animal_name
        self.hidden_animal_type = animal_type
        self.hidden_animal_age = animal_age
        self.hidden_animal_diet = animal_diet

    # 自定义方法 | Custom method
    def info(self):
        print('info=', self.hidden_animal_name, self.hidden_animal_type, self.hidden_animal_age,
              self.hidden_animal_diet)

    '''
    定义 getter&setter方法 | Define getter & setter method
    get_xxx()方法 用来获取对象属性
    set_xxx()方法 用来修改对象属性
    '''

    def get_animal_name(self):
        return self.hidden_animal_name

    def set_animal_name(self, animal_name):
        self.hidden_animal_name = animal_name

    def get_animal_type(self):
        return self.hidden_animal_type

    def set_animal_type(self, animal_type):
        self.hidden_animal_type = animal_type

    def get_animal_age(self):
        return self.hidden_animal_age

    def set_animal_age(self, animal_age):
        if animal_age > 0:
            self.hidden_animal_age = animal_age

    def get_animal_diet(self):
        return self.hidden_animal_diet

    def set_animal_diet(self, animal_diet):
        self.hidden_animal_diet = animal_diet


# 创建实例 | Create instance
animals_1 = Animals()

# 为实例赋值 | Assigning values ​​to instances
animals_1.set_animal_name('Cat')
animals_1.set_animal_type('Feline')
animals_1.set_animal_age(10)
animals_1.set_animal_diet('Fish')

# 调用 方法 | Call method
animals_1.info()


# Property 装饰器 | property decorator
# 定义 类 | Definition class
class Zoo():
    # 定义 初始化方法 | Definition initialization method
    def __int__(self, animal_name, animal_type, animal_age, animal_diet):
        self._animal_name = animal_name
        self._animal_type = animal_type
        self._animal_age = animal_age
        self._animal_diet = animal_diet

    # 自定义方法 | Custom method
    def info(self):
        print('info=', self._animal_name, self._animal_type, self._animal_age, self._animal_diet)

    # 定义 getter&setter方法 | Define getter & setter method
    @property
    def animal_name(self):
        return self._animal_name

    @property
    def animal_type(self):
        return self._animal_type

    @property
    def animal_age(self):
        return self._animal_age

    @property
    def animal_diet(self):
        return self._animal_diet

    @animal_name.setter
    def animal_name(self, animal_name):
        self._animal_name = animal_name

    @animal_type.setter
    def animal_type(self, animal_type):
        self._animal_type = animal_type

    @animal_age.setter
    def animal_age(self, animal_age):
        self._animal_age = animal_age

    @animal_diet.setter
    def animal_diet(self, animal_diet):
        self._animal_diet = animal_diet


# 创建实例 | Create instance
z = Zoo()

# 为实例赋值 | Assigning values ​​to instances
z.animal_name = 'lion'
z.animal_type = 'Feline'
z.animal_age = 12
z.animal_diet = 'Meat'

# 调用 方法 | Call method
z.info()

# 调用 属性 | # 调用 属性
print('animal_name=', z.animal_name)
print('animal_type=', z.animal_type)
print('animal_age=', z.animal_age)
print('animal_diet=', z.animal_diet)


# 继承 | inherit
# 定义 父类 | Definition father class
class Cars:
    # 定义 汽车信息 方法 | Definition car information method
    def car_info(self):
        print('Car info')


# 定义子类  继承父类 | Defining subclasses inheriting parent classes
class BMW(Cars):
    def bmv_info(self):
        print('BMW info')

    # 方法重写 | Method rewrite
    def car_info(self):
        print('Car info = BMW')


# 创建实例 | Create instance
bmw = BMW()

# 子类实例 调用方法 | Subclass instance call method
bmw.car_info()
bmw.bmv_info()

# 检查对象实例 | Check object instance
instance_res1 = isinstance(bmw, Animals)
instance_res2 = isinstance(bmw, Cars)
instance_res3 = isinstance(bmw, BMW)
print('instance_res1=', instance_res1)
print('instance_res2=', instance_res2)
print('instance_res3=', instance_res3)

# issubclass() 检查一个类是否是另一个类的子类
issubclass_res1 = issubclass(BMW, Animals)
issubclass_res2 = issubclass(Cars, BMW)
issubclass_res3 = issubclass(BMW, Cars)
issubclass_res4 = issubclass(Cars, object)
issubclass_res5 = issubclass(BMW, object)
print('issubclass_res1=', issubclass_res1)
print('issubclass_res2=', issubclass_res2)
print('issubclass_res3=', issubclass_res3)
print('issubclass_res4=', issubclass_res4)
print('issubclass_res5=', issubclass_res5)


# 调用 方法优先级 | Call method priority
# 定义 父类 A | Definition father class A
class A(object):
    def cores(self):
        print('AAA')


# 定义 子类 B 继承 父类 A | Definition subclass B inherits parent class A
class B(A):
    def cores(self):
        print('BBB')


# 定义 子类 C 继承 B | Definition subclass C inherits B
class C(B):
    def cores(self):
        print('CCC')


# 创建实例 | Create instance
c = C()

# 调用方法 | Calling method
c.cores()  # OutPut CCC


# super()
# 定义 父类 | Definition father class
class Car:
    # 定义 初始化方法 | Definition initialization method
    def __int__(self, car_name):
        self._car_name = car_name

    # 定义 getter&setter方法 | Define getter & setter method
    @property
    def car_name(self):
        return self._car_name

    @car_name.setter
    def car_name(self, car_name):
        self._car_name = car_name

    # 定义 汽车信息 方法 | Definition car information method
    def car_info(self):
        print('Car info')


# 定义子类  继承父类 | Defining subclasses inheriting parent classes
# 父类中的所有方法都会被子类继承, 包括特殊方法, 但也可以重写特殊方法
class Bmw(Car):
    # 定义 初始化方法 | Definition initialization method
    def __init__(self, car_name, car_colour):
        self._car_colour = car_colour
        # 调用 父类方法 | Call parent method
        super().__int__(car_name)

    # 定义 getter&setter方法 | Define getter & setter method
    @property
    def car_colour(self):
        return self._car_colour

    @car_colour.setter
    def car_colour(self, car_colour):
        self._car_colour = car_colour

    def bmv_info(self):
        print('BMW info=', self._car_name, self._car_colour)

    # 方法重写 | Method rewrite
    def car_info(self):
        print('Car info = BMW')


# 创建实例 | Create instance
bmw = Bmw('bmw M6', 'blue')

# 子类实例 调用方法 | Subclass instance call method
bmw.car_info()
bmw.bmv_info()

# 多重继承 | Multiple inheritance

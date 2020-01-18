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


# 面向对象 (继承) | Object-oriented (inherited)
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
# 定义 父类 D | Definition father class D
class D(object):
    def cores(self):
        print('DDD')


# 定义 子类E  | Definition subclass E
class E(object):
    def cores(self):
        print('EEE')


# 定义 子类 F 多重继承 D E | Definition Subclass F Multiple inheritance D E
class F(D, E):
    def cores(self):
        print('FFF')


# 获取当前类的所有父类 | Get all parent classes of the current class
print('F.__bases__ =', F.__bases__)

# 创建实例 | Create instance
f = F()

# 调用方法 | Calling method
f.cores()  # OutPut FFF


# 面向对象 (多态) | Object-oriented (polymorphic)
# 定义 类 | Definition class
class G:
    def __init(self, infos):
        self._infos = infos

    @property
    def infos(self):
        return self._infos

    @infos.setter
    def infos(self, infos):
        self._infos = infos


# 定义 类 | Definition class
class H:
    def __init(self, infos):
        self._infos = infos

    @property
    def infos(self):
        return self._infos

    @infos.setter
    def infos(self, infos):
        self._infos = infos


# 定义 类 | Definition class
class J:
    pass


# 创建实例 | Create instance
g = G()
h = H()

# 为实例赋值 | Assigning values ​​to instances
h.infos = 'H'
g.infos = 'G'


# 定义 全局函数 | Definition global function
def info(obj):
    # 定义 类型检查 | Definition type checking
    '''
    该函数只有obj是G类型的对象时才可以正常使用
    其他类型的对象都无法使用该函数, 这个函数就违反了多态,
    违反了多态的函数, 只适用于一种类型的对象, 无法处理其他类型对象, 这样导致函数的适应性非常差
    注意: isinstance()此函数在开发中一般是不会使用
    :param obj:
    :return:
    '''
    if isinstance(obj, G):
        print('infos =', obj.infos)
    else:
        print("no info!")


# 调用函数 | call function
info(g)


# 类中的属性 & 方法 | Properties & methods in the class
# 定义 类 | Definition class
# 类中可以包含: 类属性 / 实例属性 / 类方法 / 实例方法 / 静态方法
class K(object):
    # 定义 属性 | Definition attribute
    '''
    可以直接在类中定义的属性就称之为类属性
    类属性可以通过类或实例进行访问
    但是类属性只能通过类对象进行修改, 无法通过实例对象进行修改
    '''
    res_sum = 0

    # 定义 初始化方法 | Definition initialization method
    '''
    通过实例对象添加的属性属于实例属性
    实例属性只能通过实例对象进行访问和修改, 类对象无法进行访问修改
    '''

    def __init__(self):
        self.infos = 'Info'

    # 定义 实例方法 | Defining instance methods
    '''
    在类中定义以`seIf`为第一个参数的方法称之为实例方法
    实例方法在调用时Python解析器会将调用对象作为`seIf`传入
    实例方法可以通过实例和类进行调用
    当通过实例调用时, 会自动将当前调用对象作为`seIf`传入
    当通过对象调用时, 不会自动传入`seIf`, 必须需要开发者手动传递`seIf`
    '''

    def core_info(self):
        print('core_info=', self)

    # 定义 类方法 | Definition class method
    '''
    在类内部使用`@classmethod`关键字来修饰类方法
    类方法中第一个参数为`cls`, `cls`参数也会被自动传递, `cls`就是当前类的对象
    类方法和实例方法的区别在于: 实例方法第一个参数为`seIf`, 而类方法第一个参数为`cls`
    类方法可以通过类进行调用, 也可以通过实例进行调用
    '''

    @classmethod
    def core_cls(cls):
        print('core_cls=', cls, cls.res_sum)

    # 定义 静态方法 | Definition static method
    '''
    在类中使用`@staticmethod`关键字来修饰静态方法
    静态方法不需要指定任何的默认参数, 静态方法可以通过类和实例进行调用
    静态方法基本上是和当前类无关的方法, 它只是存储当前类中的函数, 该方法一般在开发中作为工具方法使用
    '''

    @staticmethod
    def core_staticmethod():
        print('core_staticmethod')


# 创建实例 | Create instance
k = K()

k.res_sum = 1000
K.res_sum = 10000

print('k', k.res_sum)
print('K', K.res_sum)

k.core_info()
K.core_info(k)

k.core_staticmethod()
K.core_staticmethod()


# 垃圾回收 | Garbage collection
# 定义 类 | Definition class
class U:
    # 定义 初始化方法 | Definition initialization method
    def __init__(self):
        self.info = 'U class'

    # 定义 del特殊方法, 在对象被垃圾回收前调用该方法
    def __del__(self):
        print('Delete U class', self)


# 创建实例 | Create instance
u = U()

'''
垃圾回收 测试 | 将u实例定义为空, 此时只要没有任何变量对U对象进行引用, 则该实例在内存中就变成了垃圾, Python将自动进行垃圾回收
'''
a = None


# 特殊方法 | Special method
# 定义 类 | Definition class
class Shape:
    # 定义 初始化方法 | Definition initialization method
    def __init__(self, name, lengths):
        self.name = name
        self.lengths = lengths

    '''
    `__str__()` 该特殊方法会在尝试将对象转换为字符串时调用
    该作用是可以用来指定对象转换为字符串的结果
    '''

    def __str__(self):
        return 'Shape [Name= %s , Lengths= %d]' % (self.name, self.lengths)

    '''
    `__repr__()` 该特殊方法会在对当前对象使用`repr()`函数时调用
    该作用是指定对象在`交互模式`中直接输出返回结果
    '''

    def __repr__(self):
        return 'This is the graphics class!'

    '''
    其他特殊方法介绍 | Introduction of other special methods
    
    `object.__lt__(self, other)` 小于 < 
    该特殊方法在对象进行小于比较时调用, 该方法返回值将作为比较结果进行返回, 
    该方法需要携带两个参数, `self`参数则表示当前对象, `other`参数则表示和当前对象比较的对象
    
    `object.__le__(self, other)` 小于等于 <=
    该特殊方法在对象进行小于等于比较时调用, 该方法返回值将作为比较结果进行返回, 
    该方法需要携带两个参数, `self`参数则表示当前对象, `other`参数则表示和当前对象比较的对象
    
    `object.__eq__(self, other)` 等于 ==
    该特殊方法在对象进行等于比较时调用, 该方法返回值将作为比较结果进行返回, 
    该方法需要携带两个参数, `self`参数则表示当前对象, `other`参数则表示和当前对象比较的对象
    
    `object.__ne__(self, other)` 不等于 !=
    该特殊方法在对象进行不等于比较时调用, 该方法返回值将作为比较结果进行返回, 
    该方法需要携带两个参数, `self`参数则表示当前对象, `other`参数则表示和当前对象比较的对象
    
    
    `object.__gt__(self, other)` 大于 >
    该特殊方法在对象进行大于比较时调用, 该方法返回值将作为比较结果进行返回, 
    该方法需要携带两个参数, `self`参数则表示当前对象, `other`参数则表示和当前对象比较的对象
    
    
    `object.__ge__(self, other)` 大于等于 >=
    该特殊方法在对象进行大于等于比较时调用, 该方法返回值将作为比较结果进行返回, 
    该方法需要携带两个参数, `self`参数则表示当前对象, `other`参数则表示和当前对象比较的对象
    '''

    def __lt__(self, other):
        return self.lengths < other.lengths

    def __le__(self, other):
        return self.lengths <= other.lengths

    def __eq__(self, other):
        return self.lengths == other.lengths

    def __ne__(self, other):
        return self.lengths != other.lengths

    def __gt__(self, other):
        return self.lengths > other.lengths

    def __ge__(self, other):
        return self.lengths >= other.lengths


# 创建实例 | Create instance
s1 = Shape('Round', 158)
s2 = Shape('Rectangle', 412)

# 当打印对象时实际上打印的是对象的中特殊方法`__str__()`的返回值
print('s1=', s1)  # s1= <__main__.Shape object at 0x10b524a60>
print('s2=', s2)  # s2= <__main__.Shape object at 0x10b524ac0>

# 小于比较 | Less than comparison
print('s1 < s2 =', s1 < s2)  # s1 < s2 = True
print('s2 < s1 =', s2 < s1)  # s2 < s1 = False

# 小于等于比较 | Less than or equal comparison
print('s1 <= s2 =', s1 <= s2)  # s1 <= s2 = True
print('s2 <= s1 =', s2 <= s1)  # s2 <= s1 = False

# 等于比较 | Equal comparison
print('s1 == s2 =', s1 == s2)  # s1 == s2 = False
print('s2 == s1 =', s2 == s1)  # s1 == s2 = False

# 不等于比较 | Not equal to compare
print('s1 != s2 =', s1 != s2)  # s1 != s2 = True
print('s2 != s1 =', s2 != s1)  # s2 != s1 = True

# 大于比较 | Greater than comparison
print('s1 > s2 =', s1 > s2)  # s1 > s2= False
print('s2 > s1 =', s2 > s1)  # s2 > s1= True

# 大于等于比较 | Greater than or equal
print('s1 >= s2 =', s1 >= s2)  # s1 >= s2 = False
print('s2 >= s1 =', s2 >= s1)  # s2 >= s1 = True

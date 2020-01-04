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
# @Program : 数据结构集合 | Data structure collection
# @File : 09_data_structure_collection.py
# @Description : Python 基础篇 - 数据结构集合 | Python Basics-Data Structure Collection

# 定义 列表 | Definition list
list1 = [1, 2, 3, 4, 5]

# 获取列表元素长度 | Get list element length
print('lens=', len(list1))

# 访问列表中的值 | Access value in list
print(list1[1])

# 更新列表 | update list
list1.append(6)

# 向列表指定位置插入元素 | Insert an element at a specified position in the list
list1.insert(3, 7)

# 使用新的序列扩展当前序列 | Extend current sequence with new sequence
list1.extend([8, 9])

# 定义 迭代列表元素 | Definition iteration
for data in list1:
    print('data=', data)

# 删除列表元素 | Remove list element
del list1[2]

# 根据索引删除指定元素并返回被删除元素的值 | Deletes the specified element based on the index and returns the value of the deleted element
delete_value = list1.pop(3)
print('delete_value=', delete_value)

# 根据指定元素删除元素值 | Delete element value based on specified element
list1.remove(5)

# 将列表元素反转 | Reverse list element
list1.reverse()

# 对列表元素进行排序,默认为升序排序 | Sort list elements, default is ascending
list1.sort()
list1.sort(reverse=True)

# 清空列表 | clear the list
list1.clear()

print('list1=', list1)

# 定义 列表切片 | Definition list slice
# 如果省略结束位置则会一直截取到最后 | If the end position is omitted, it will be intercepted to the end.
print('list1[1:]: ', list1[1:])
# 如果省略起始位置则会从第一个元素开始截取 | If the starting position is omitted, it will be truncated from the first element
print('list1[:3]: ', list1[:3])
# 如果起始位置和结束位置全部省略则相当于创建一个列表的副本
print('list1[:]: ', list1[:])
# 通过切片获取元素时会包括起始位置的元素,不会包括结束位置的元素
print('list1[1:5]: ', list1[1:5])
# 定义 步长 | Definition Stride
print('list1[1:4:1]: ', list1[1:4:1])
print('list1[::1]: ', list1[::-1])

# 定义 列表 | Definition list
list2 = [1, 2, 3, 4, 5, 6]
list3 = ['C', 'C++', 'C#', 'Html', 'Java', 'PHP', 'Python', 'Scala', 'GoLang', 'R', 'Ruby', 'SQL']

# 定义 元素是否存在于列表中 | Defines whether the element exists in the list
print('Python' in list3)
print('Python' not in list3)

# 定义 迭代 | Definition iteration
for data in list3:
    print('data=', data)

# 定义 组合列表 | Definition Combination list
list2 = [1, 2, 3, 4, 5, 6] + [7, 8, 9, 10, 11]

# 定义 重复列表 | Definition repeat list
list3 = list3 * 4

# 获取列表长度 | Get list length
print('list2 length=', len(list2))
print('list3 length=', len(list3))

# 集合 综合演示 | Collection Comprehensive Demo
# 定义 接收 用户名 组件 | Definition receive username component
user_name_input = input('\nPrompt: Please enter UserName....\n')
# 对用户输入用户名进行校验 | Verify user input username
if user_name_input == 'system' or user_name_input == 'System':
    print('‖-------------------------------------------------‖')
    print('\n‖ Prompt: Username Verification Successful !', user_name_input, '..... ‖\n')
    print('‖-------------------------------------------------‖\n')
    # 定义 接收 组件 | Definition receiving component
    user_password_input = input('\nPrompt: Please enter Password....\n')
    # 对用户输入密码进行校验 | Verify user input password
    if user_password_input == 'xxx':
        print('‖-------------------------------------------------‖')
        print('\n‖ Prompt: Password Verification Successful', user_name_input, '..... ‖\n')
        print('‖-------------------------------------------------‖')
        # 定义 令牌 组件 | Define the token component
        user_token_input = input('\nPrompt: Please enter Token....\n')
        # 对用户输入令牌进行校验 | Verify user input token
        if user_token_input == '000000':
            print('‖-------------------------------------------------‖')
            print('\n‖ Prompt: Token Verification Successful, Welcome', user_name_input, '! ‖\n')
            print('‖-------------------------------------------------‖\n')
            print(f"Prompt: Information Management System（1.Select | 2.Add | 3.Delete | 4.Quit)")
            # 定义 选择器 组件 | Define selector component
            user_value_input = input('\nPrompt: Please enter options....\n')
            # 定义 元数据信息 | Definition Metadata Information
            base_data = ['Andrew', 'Christopher', 'Ethan', 'Joshua', 'Matthew', 'Michael', 'William', 'Vivienne',
                         'Lillian', 'Linda', 'Rebecca']
            while True:
                # 根据选项1执行查询数据 | Query data according to option 1
                if user_value_input == '1':
                    for select_value in base_data:
                        print('Prompt: The query data is as follows:', select_value)
                    break
                # 根据选项2执行添加数据 | Add data according to option 2
                elif user_value_input == '2':
                    # 定义 添加数据 子组件 | Definition add data subcomponent
                    user_add_input = input('\nPrompt: 请输入添加选项.... (1.新增信息 | 2.指定位置新增信息)\n')
                    if user_add_input == '1':
                        user_new_data_input = input('\nPrompt: 请输入添加内容....\n')
                        base_data.append(user_new_data_input)
                        print('\nPrompt: 添加成功! 已刷新数据...\n')
                        for select_value in base_data:
                            print('Prompt: The query data is as follows:', select_value)
                        continue
                    elif user_add_input == '2':
                        # 定义 添加数据 (添加位置)子组件 | Definition Add data (add location) subcomponent
                        user_add_position_input = int(input('\nPrompt: 请输入数字插入的位置....\n'))
                        # 定义 添加数据 (添加数据)子组件 | Definition Add data (add data) subcomponent
                        user_add_data_input = input('\nPrompt: 请输入添加内容....\n')
                        base_data.insert(user_add_position_input, user_add_data_input)
                        print('\nPrompt: 添加成功! 已刷新数据...\n')
                        for select_value in base_data:
                            print('Prompt: The query data is as follows:', select_value)
                            continue
                    else:
                        # 输出错误警告 | Output error warning
                        print("Warning: Incorrect input, please try again!")
                # 根据选项3执行删除数据 | Delete data according to option 3
                elif user_value_input == '3':
                    # 定义 删除数据 子组件 | Definition delete data subcomponent
                    user_del_input = input('\nPrompt: 请输入删除选项.... (1.指定删除信息 | 2.清空全部信息)\n')
                    if user_del_input == '1':
                        user_remove_input = input('\nPrompt: 请输入删除内容....\n')
                        if user_remove_input == user_remove_input:
                            print('\nPrompt: ', user_remove_input, '删除成功! 已刷新数据...\n')
                            base_data.remove(user_remove_input)
                            for select_value in base_data:
                                print('Prompt: The query data is as follows:', select_value)
                                continue
                        else:
                            # 输出错误警告 | Output error warning
                            print("Warning: Incorrect input, please try again!")
                    elif user_del_input == '2':
                        user_del_data_input = input('\nDangerous operation: 请确定清空全部数据, 删除后不可恢复!!!  (y or n)\n')
                        if user_del_data_input == 'y':
                            print('已删除全部数据!')
                            base_data.clear()
                            print('\nPrompt: 已刷新数据...\n')
                            for select_value in base_data:
                                print('Prompt: The query data is as follows:', select_value)
                            continue
                        elif user_del_data_input == 'n':
                            print('已取消删除全部数据!')
                            continue
                        else:
                            # 输出错误警告 | Output error warning
                            print("Warning: Incorrect input, please try again!")
                    else:
                        # 输出错误警告 | Output error warning
                        print("Warning: Incorrect input, please try again!")
                # 根据选项4执行退出程序 | Execute exit procedure according to option 4
                elif user_value_input == '4':
                    print('Prompt: Exited the information management system !')
                    break
                else:
                    # 根据选项无匹配数值则返回程序重新输入
                    print("Warning: Incorrect input, please try again!")
        else:
            # 输出错误警告 | Output error warning
            print('\n', user_token_input, 'Warning: Token Error! Please rerun the program')
    else:
        # 输出错误警告 | Output error warning
        print('\n', user_password_input, 'Warning: Password Error!')
else:
    # 输出错误警告 | Output error warning
    print('\n', user_name_input, 'Warning: UserName Error!')

# 定义ragne() 生成自然数的序列函数 | Definition ragne() Sequence function to generate natural numbers
r1 = range(5)
r2 = range(0, 10, 2)

print('r1=', r1, list(r1))
print('r2=', r2, list(r2))

for x in range(60):
    print('r3 =', x)

# 定义 元祖 | Definition Tuple
# 创建元祖 | Create Tuple
tuples1 = (1, 2, 3, 4, 5, 6, 7, 8)
# 创建 无关闭分隔符 元祖 | Created without closing separator
tuples2 = 1, 2, 3, 4, 5, 6, 7, 8

# 定义 元祖解包 将元祖中每一个元素赋值给每一个变量
a, b, c, d, e, f, g, h = tuples2
a, b, *c = tuples1
print('a=', a)
print('b=', b)
print('c=', c)
print('d=', d)
print('e=', e)
print('f=', f)
print('g=', g)
print('h=', h)

# 修改元组 | Modify tuple
tuples3 = 9, 10, 11
tuples4 = tuples2 + tuples3
print('tuples4=', tuples4)

# 删除元组 | Delete tuple
del tuples4

# 访问元组 | Access tuple
print('tuples1[0]=', tuples1[0])
print('tuples2[0:5]=', tuples2[0:5])
print('tuples2=', tuples2)

# 定义 字典 | Definition dictionary
# 创建 字典 | Create dictionary
d1 = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H'}
d2 = dict([('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('e', 'E'), ('f', 'F'), ('g', 'G'), ('h', 'H')])
d3 = {'j': 'J', 'k': 'K', 'l': 'L'}
# 获取字典中键值对个数 | Get the number of key-value pairs in the dictionary
print('d1_len=', len(d1))

# 访问字典中的值 | Accessing values ​​in a dictionary
print("d1['b']=", d1['b'])

# 通过方法访问字典中的值 | Accessing values ​​in a dictionary via methods
print("d1.get('b')=", d1.get('b'))
print("d1.get('j')=", d1.get('j', 'defaults'))

# 修改字典 | Modify dictionary
d1['h'] = 'h'
d1.setdefault('g', 'G')
d1.setdefault('i', 'I')
d1.update(d3)
print('d1=', d1)

# 删除字典元素 | Delete dictionary element
del d1['a']
d1.popitem()
d1.pop('f')
print("d1.pop('z')", d1.pop('z', 'defaults'))
print('d1=', d1)
d2.clear()
print('d2=', d2)

# 字典浅复制 | Dictionary shallow copy
d4 = {'m': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q'}
# 复制后的对象和原对象是完全独立的, 两个对象之间的变化不会影响
d5 = d4.copy()
print('d4=', d4, 'd4_id=', id(d4))
print('d5=', d5, 'd5_id=', id(d5))

# 遍历 字典 | Traversal dictionary
# 调用keys()方法, 该方法将返回一个序列, 该序列中保存字典中所有的键
for k1 in d4.keys():
    print('key=', k1, 'value=', d4[k1])

# 调用values()方法, 该方法将返回一个序列, 该序列中保存字典中所有的值
for v1 in d4.values():
    print('v1=', v1)

# 调用items()方法, 该方法会返回一个(字典中所有项)的序列, 序列中包含双值子序列
for k2, v2 in d4.items():
    print('res=', k2, '=>', v2)

# 定义 集合 | Definition collection
# 创建 集合 | Create collection
s1 = set()  # 定义 空set集合 | Definition empty set collection
s2 = {'a', 'c', 'd', 'r', 'g', 'p'}
s3 = set([1, 2, 5, 6, 8])  # 调用set()方法将列表转换为集合
s4 = set([(1, 2, 3, 4), (6, 8, 7, 10)])  # 调用set()方法将元祖转换为集合
s5 = set({'a': 'A', 'b': 'B', 'c': 'C'})  # 调用set()方法将字典转换为集合, 但包含字典中的键
s6 = set('Python')  # 调用set()方法将字符串转换为集合

print('s1=', s1, '\t s2=', s2)
print('s3=', s3, '\t s4=', s4)
print('s5=', s5, '\t s6=', s6)

# 获取集合元素个数 | Get the number of collection elements
print('len(s5)=', len(s5))

# 检查集合中的指定元素 | Check specified element in collection
print('d' in s5)

# 向集合中添加元素 | Add elements to the collection
s2.add('k')
s2.update(s4)
s2.update(s5)
s2.update(s6)
print('s2=', s2)

# 删除集合 | Remove collections and elements
# 随机删除集合元素 | Remove collection elements randomly
s5.pop()
print('s5=', s5)

# 指定删除集合元素 | Specifies to delete collection elements
s5.remove('a')
print('s5=', s5)

# 清空集合所有元素 | Clear all elements of the collection
s6.clear()
print('s6=', s6)

# 集合 浅复制 | Collection shallow copy
s7 = set([1, 2, 5, 6, 8])
# 复制后的对象和原对象是完全独立的, 两个对象之间的变化不会影响
s8 = s7.copy()
print('s7=', s7, 's7_id=', id(s7))
print('s8=', s8, 's8_id=', id(s8))

# 集合 运算 | Set operation
s9 = {1, 2, 3, 4, 5}
s10 = {1, 2, 3, 4, 5, 6, 7}

# `&` 交集运算 | `&` Intersection operation
res1 = s9 & s10
print('Intersection_Operation=', res1)  # Output result: Intersection_Operation= {3, 4, 5}

# `|` 并集运算 | `|` Union Set Operation
res2 = s9 | s10
print('Union_Set_Operation=', res2)  # Output result: Union_Set_Operation= {1, 2, 3, 4, 5, 6, 7}

# `-` 差集运算 | `-` Difference Set Operation
res3 = s9 - s10
print('Difference_Set_Operation=', res3)  # Output result: Difference_Set_Operation= {1, 2}

# `^` 异或集运算 | `^` XOR set operation
res4 = s9 ^ s10
print('XOR_Set_Operation=', res4)  # Output result: XOR_Set_Operation= {1, 2, 6, 7}

# `<=` 检查集合是否为另一个集合的子集 | `<=` Checks if a collection is a subset of another collection
# 如果a集合中的元素全部在b集合中出现, 则a集合称之为b集合的子集, b集合即使a集合的超集
collection_subset = s9 <= s10
print('Collection_Subset=', collection_subset)  # Output result: Collection_Subset= True

# `<` 检查集合是否为另一个集合的真子集 | `<` Checks if a set is a true subset of another set
# 如果超集b中含有子集a中的所有元素, 并且b中包含a中没有的元素则称之b为真超集, a是b的真子集
res5 = {1, 2, 3} < {1, 2, 3, 4, 5}
print('res5=', res5)  # res5= True

# `>=` 检查集合是否为另一个集合的超集 | `> =` Checks if a collection is a superset of another collection
res6 = s9 >= s10
print('res6=', res6)  # res6= False

# `>` 检查集合是否为另一个集合的真超集 | `>` Check if a collection is a true superset of another collection
res7 = s9 > s10
print('res7=', res7)  # res7= False

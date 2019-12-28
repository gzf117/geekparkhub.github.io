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
# @Program : 流程控制 | Process control
# @File : 08_process_control.py
# @Description : Python 基础篇 - 流程控制 | Python Basics - Process control

# 流程控制 | Process control

# 定义 条件判断语句 | Definition Conditional Judgment
if True:
    print("Output_1")
    print("Output_2")
    print("Output_3")


# 定义 身份验证函数 | Define authentication function
def verification(user_name_input, user_password_input, user_token_input):
    # print('\nPlease enter UserName....')
    if user_name_input == 'system' or user_name_input == 'System':
        print('‖-------------------------------------------------‖')
        print('\n‖ Username Verification Successful !', user_name_input, '..... ‖\n')
        print('‖-------------------------------------------------‖\n')
        # print('\nPlease enter Password....\n')
        if user_password_input == 'xxx':
            print('‖-------------------------------------------------‖')
            print('\n‖ Password Verification Successful', user_name_input, '..... ‖\n')
            print('‖-------------------------------------------------‖')
            # print('\nPlease enter Token....\n')
            if user_token_input == '000000':
                print('‖-------------------------------------------------‖')
                print('\n‖ Token Verification Successful, Welcome', user_name_input, '! ‖\n')
                print('‖-------------------------------------------------‖')
            else:
                print('\n', user_token_input, 'Token Error!')
        else:
            print('\n', user_password_input, 'Password Error!')
    else:
        print('\n', user_name_input, 'UserName Error!')


# 定义 参数 | Definition parameter
name = input('\nPlease enter UserName....\n')
password = input('\nPlease enter Password....\n')
token = input('\nPlease enter Token....\n')

# 调用 身份验证函数 | Transfer authentication function
verification(name, password, token)

# 定义 循环语句 | Definition loop statement

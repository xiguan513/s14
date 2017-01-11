#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
    输入用户名密码
    认证成功后显示欢迎信息
    输错三次后锁定
    提供管理员解锁

"""

Flag_user=True

user_pass={"song":123456,
           "admin":123456,
           "bing":123456}
import fileinput

file_lock="passwd"



while Flag_user:
    pass_num = 0 #设置标志位
    login_name=input("Please input your name: ").strip()

    if login_name in user_pass:#判断用户是否存在
        with open(file_lock) as lock_file:
            lock_list=lock_file.readlines()
        if [ user for user in lock_list if login_name in user.strip()  ]:#通过列表表达式判断是否在黑名单
            print("This user has been locked")
            continue
    else:
        print("Not Found User!")
        continue

    while 3 > pass_num:  # 判断用户密码输入次数
        login_pass = int(input("Please input your password: "))
        if login_pass == user_pass[login_name]:  # 判断密码是否正确
            print("Welcome")
            if login_name == "admin":
                unlock_user = input("Please inpur your unlock user: ")
                for user in fileinput.input(file_lock, backup=".bak", inplace=1):#清除黑名单用户
                    print(user.rstrip().replace(unlock_user, ''))#fileinput 替换方法
            break
        else:
            pass_num += 1
            print("password is  error")
    else:
        print("Wrong password three times, lock user")
        with open("passwd", "a+") as lock_user:  # 添加黑名单
            lock_user.write("\r")
            lock_user.write(login_name)
        continue
    break


if __name__ == '__main__':
    pass


#!/usr/bin/env python
# -*- coding: UTF-8 -*-

Flag_user=True

user_pass={"song":123456,
           "admin":123456,
           "bing":123456}
import sys

while Flag_user:
    pass_num = 0 #设置标志位
    login_name=input("Please input your name: ").strip()
    if login_name in user_pass:#判断用户是否存在
        with open("passwd") as lock_file:
            for line in lock_file.readlines():
                if login_name  in line.strip():#判断是否在黑名单
                    print("This user has been locked")
                    sys.exit()
        while 3>pass_num:#判断用户密码输入次数
            login_pass=int(input("Please input your password: "))
            if login_pass == user_pass[login_name]:#判断密码是否正确
                print("Welcome")
                break
            else:
                pass_num+=1
                print("password is  error")
        else:
            print("Wrong password three times, lock user")
            with open("passwd", "a+") as lock_user:#添加黑名单
                lock_user.write("\r")
                lock_user.write(login_name)
            continue
        break
    else:
        print("Not Found User!")
        continue





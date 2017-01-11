#!/usr/bin/env python
# -*- coding: UTF-8 -*-


name_uesr={"song":123456,
           "bing":123456,
           "admin":123456}


while True:
    login_name=input("Please input your name: ").strip()
    if login_name in name_uesr:
        while True:
            try:
                login_name_pass=int(input("Please input your this user passwd: "))
                if login_name_pass==name_uesr[login_name]:
                    print("Welcome to shop!")
            except ValueError:
                print("password is error")
    else:
        print("Sorry not to find this user!")

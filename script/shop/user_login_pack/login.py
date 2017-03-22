#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import sys
import my_conf
from shop.shop_pack import shopping

sql_name= my_conf.select_user

def login_user():
    while True:
        login_name=raw_input("Please enter your login name:").strip()
        if login_name:
            if sql_name(login_name):
                print "此用户存在"
                while True:
                    login_pass=raw_input("Please enter your loging passwd:").strip()
                    #print login_pass

                    if login_pass:
                        usre_pass=my_conf.select_pass(login_name,login_pass)
                        #print usre_pass
                        if usre_pass== "black":
                            break
                        elif usre_pass=="登录成功":
                            print "登录成功"
                            #shopping.user_shop()
                            shopping.buy_shop(login_name)
                            sys.exit()
                        elif usre_pass=="密码错误":
                            print "密码错误登录失败"
                            #continue
                    else:
                        print "密码不能为空"
            else:
                print "谢谢光临"
                sys.exit()
        else:
            print "不允许为空"


if __name__ == '__main__':
    login_user()


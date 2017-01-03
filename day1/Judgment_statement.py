#!/usr/bin/env python
# -*- coding: UTF-8 -*-


name="song"
username=input("Please input your name: ")
if username==name:
    print("My name is {username}".format(username=username))
else:
    print("Sorry not found user!")



get_achievement=input("Please input your achievement: ")

if get_achievement.isdigit():
    get_achievement=int(get_achievement)
    if 60<=get_achievement<=70:
        print("Your grades have passed.")
    elif  70<=get_achievement<=80:
        print("Your grades are good.")
    elif 80<get_achievement<=100:
        print("Your grades are excellent.")
    elif 100<get_achievement:
        print("error grades!")
    else:
        print("You need to work hard")
else:
    print("Please input number!")






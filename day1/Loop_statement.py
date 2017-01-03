#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# for i in  list(range(1,10)):
#     print("\r")
#     print(i,end=" ")
#     for a in 'spam':
#         print(a,end=" ")


# for i in list(range(1,10)):
#     for j in list(range(1,i+1)):
#         print("%dx%d=%d" % (j,i,j*i),end=" ")
#         if j==i:
#             print("\r")




number=10

Flag=True
while Flag:
    get_number = input("Please input your lucky number: ")
    if get_number.isdigit():
        get_number=int(get_number)
    else:
        print("need number!")
        continue
    if get_number==number:
        print("This is your lucky number!")
        Flag=False
    elif get_number>number:
        print("The number you entered is too large")
    elif get_number<number:
        print("The number you entered is too small.")
else:
    print("game over!")
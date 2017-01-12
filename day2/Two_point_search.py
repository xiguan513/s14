#!/usr/bin/env python
# -*- coding: UTF-8 -*-

num_list=list(range(1,100))
#print(num_list)

num = int(input("Enter the number you want to find: "))
def two(list,num):
    mid=int(len(list)//2)#取出列表的下标,以便后面根据下标获取对应的值
    if list[mid] >= 1:
        if list[mid] > num: #判断下标对应的数字是否大于我输入的数字
            two_list = list[:mid] #如果下标对应的数字是大于我输入的数字，取出开始到我下标位置的数字，保存为新的列表
            print(two_list)
            return two(two_list,num)#递归重新带入计算
        elif list[mid] < num:#判断下标对应的数字是否小于我输入的数字
            two_list = list[mid:]#如果下标对应的数字是小于我输入的数字，取出从我下标位置的数字到最后，保存为新的列表
            print(two_list)
            return two(two_list,num)#递归重新带入计算
        else:
            print(list[mid]) #如果等于就直接输出列表中的数字

if __name__=="__main__":
    two(num_list,num)
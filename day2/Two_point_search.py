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

if __name__ == "__main__":
    two(num_list, num)

#二分查找函数
import bisect

L = [1, 3, 3, 6, 8, 12, 15]


x_insert_point = bisect.bisect_left(L, num)  # 在L中查找x，x存在时返回x左侧的位置，x不存在返回应该插入的位置..这是3存在于列表中，返回左侧位置１
print(x_insert_point)

x_insert_point = bisect.bisect_right(L, num)  # 在L中查找x，x存在时返回x右侧的位置，x不存在返回应该插入的位置..这是3存在于列表中，返回右侧位置３
print(x_insert_point)


x_insort_left = bisect.insort_left(L, num)  # 将x插入到列表L中，x存在时插入在左侧
print(L)

x_insort_rigth = bisect.insort_right(L, num)  # 将x插入到列表L中，x存在时插入在右侧　　　　
print(L)


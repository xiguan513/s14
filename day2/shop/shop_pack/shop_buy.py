#!/usr/bin/env python
# -*- coding: UTF-8 -*



from s14.day2.shop.login_pack import login_api


#引用用户登录接口
#login_api.login()
with open("shop_list") as shop_file:
    #读取文件内容并把内容转换为字典格式
    shop_dit={k:i for k,i in enumerate(shop_file.readlines())}
    for k,i in shop_dit.items():
        print(k,i,end="")

print("\r")
flat=False
while True:
    wages=input("Please enter your salary：").strip()
    if wages.isdigit():
        wages=int(wages)
    else:
        print("Pleae input number!")
        continue
    shop_list_buy = []#记录已购买商品列表
    while not flat:
        shop_list_new = []#记录当前购买的商品列表及价格
        shop_num=input("Please enter the number of goods: ").strip()
        if shop_num.isdigit():
            shop_num=int(shop_num)
        else:
            continue
        if shop_num in shop_dit:
            shop_list_new.append(shop_dit[shop_num].strip("\n").split())#保存计算当前购买商品及价格，每次循环清空列表，只保留当前的数据
            #print(shop_list_new)
            if wages > int(shop_list_new[0][1]):
                wages-=int(shop_list_new[0][1])#计算已购买商品后剩余价格
                shop_list_buy.append(shop_dit[shop_num].strip("\n").split())#记录所有购买的商品列表
                print(shop_list_buy)
                print(wages)
            else:
                print("Whether the balance is insufficient to purchase other products!")
        else:
            print("商品不存在")
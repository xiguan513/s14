#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import MySQLdb
import sys

hostname = "localhost"
username = "root"
password = '123456'
dbname = "dream"

dbconn=MySQLdb.connect(
    host=hostname,
    port=3306,
    user=username,
    passwd=password,
    db=dbname,
    charset='utf8',
)

def user_shop():
    print "欢迎光临，Dream 超市!"
    shop_all="select id,shopname,shopprice from shopping"
    cursor=dbconn.cursor()
    cursor.execute(shop_all)
    alldata=cursor.fetchall()
    print "商品id\t商品名\t商品价格\n"
    #print alldata
    for shop_list in alldata:
        for i in range(len(shop_list)):
            print shop_list[i],
            if i==2:
                print '\n'

def buy_shop(user_name):
    user_shop()
    shoppingprice=0
    while True:
        shop=raw_input("请输入购买产品编号：")
        if shop.isdigit():
            sql="select id,shopname,shopprice from shopping where id='%s'" % shop
            cursor=dbconn.cursor()
            cursor.execute(sql)
            shop_list=cursor.fetchall()
            print shop_list
            insertshopping="INSERT into buy_shopping (username,buyshop,buyprice) VALUES ('%s','%s','%s')" % (user_name,shop_list[0][1],shop_list[0][2])
            cursor.execute(insertshopping)
            shoppingprice+=float(shop_list[0][2])

        elif shop=="exit":
            print "购买结束"
            sql="select totalamount from amount where username='%s'" % user_name
            cursor.execute(sql)
            totalamount=cursor.fetchall()
            totalamount=float(totalamount[0][0])
            totalamount-=shoppingprice
            updatetotalamount="UPDATE amount set totalamount='%s' where username='%s'" % (totalamount,user_name)
            cursor.execute(updatetotalamount)
            selectshopping="select buyshop from buy_shopping where username='%s'" % user_name
            cursor.execute(selectshopping)
            buyshop=cursor.fetchall()
            print buyshop

            dbconn.commit()
            print "剩余金额"
            sql = "select totalamount from amount where username='%s'" % user_name
            cursor.execute(sql)
            totalamount = cursor.fetchall()
            totalamount = float(totalamount[0][0])
            print totalamount
            sys.exit()
        else:
            print "请输入产品编号"
        print "加入购物车"

        print "购买产品总结价格"
        print shoppingprice


if __name__ == '__main__':
    buy_shop()



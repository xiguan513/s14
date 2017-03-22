#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import MySQLdb
import sys
import time
import re

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


def select_user(getname):
    cursor=dbconn.cursor()

    sql="select id,username,userpass,alisaname,sex,blacklist,phone,email,regisdates,ip from user_login where username='%s' and blacklist<=3" % getname
    #sql="select * from user_login"
    cursor.execute(sql)
    alldata=cursor.fetchall()
    if alldata:
        return alldata
    else:
        regisuser=raw_input("此用户不存在是否注册用户 y/n:")
        if regisuser=='y':
            username=raw_input("请输入注册用户名称：")
            userpass=raw_input("请输入注册用户密码：")
            alisaname=raw_input("请输入注册用户昵称：")
            while True:
                sex = raw_input("请输入注册用户性别：")
                if sex=="男" or  sex=="女":
                    break
                else:
                    print "请输入正确的性别 男或者女"
                    continue
            phone=raw_input("请输入注册用户电话：")
            while True:
                email=raw_input("请输入注册用户邮件：")
                # 邮箱匹配
                # 一 不能以 . - _ | 特殊字符串 开始,和结束
                # 二 不能是特殊字符
                # 三 只有一个@
                # 四 只有一个.
                # 五 结尾是@xxx.xxx模式
                p = re.compile('[^\W\._-][\w\.-]+@(?:[a-zA-Z0-9]+\.)+[a-zA-Z]+$')
                if p.match(email):
                    print("邮箱匹配正确")
                    break
                else:
                    print("邮箱匹配失败")
                    continue

            regisdates=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            userinset="""
            INSERT INTO `dream`.`user_login` (`id`, `username`, `userpass`, `alisaname`, `sex`, `blacklist`,`blacknum`, `phone`, `email`, `regisdates`, `ip`)
            VALUES (NULL, '%s', '%s', '%s','%s','0', '0', '%s', '%s', '%s', '192.168.0.142')
            """ % (username,userpass,alisaname,sex,phone,email,regisdates)
            cursor.execute(userinset)
            dbconn.commit()
            print "注册用户成功"
        elif regisuser=='n':
            return None
        else:
            print "请输入一个选项"
    cursor.close()
    dbconn.close()
num=0
def select_pass(getname,getpass):

    cursor=dbconn.cursor()
    sql="select id,username,userpass,alisaname,sex,blacklist,phone,email,regisdates,ip from user_login where username='%s' and userpass='%s'" % (getname,getpass)
    cursor.execute(sql)
    alldata=cursor.fetchall()
    #print alldata
    if alldata:
        blacklist="select blacknum from user_login where username='%s'" % (getname)
        cursor.execute(blacklist)
        blacknum=cursor.fetchall()
        #print blacknum
        #print blacknum
        for i in blacknum:
            i=int(i[0])
            if i>=3:
                print "此用户被禁用，请联系管理员"
                return 'black'
            #print alldata
            return "登录成功"
    else:
        global num
        num+=1
        #print num
        if num>=3:
            #print "已经超出限制"
            updatesql="UPDATE user_login SET blacknum='%s' WHERE username='%s'" % (num,getname)
            print updatesql
            cursor.execute(updatesql)
            dbconn.commit()
            num=0
            print num
        return "密码错误"
        #return None
    cursor.close()
    dbconn.close()




if __name__ == '__main__':
    #print select_user('test',123456)
    select_pass('test',123456)



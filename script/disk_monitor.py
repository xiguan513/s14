#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import sys
import pickle

disk_status=""
file_name="1221.log"
#file_name=sys.argv[1]
file=open(file_name)


ser_name={"10.172.84.70":"b2b1",
          "10.171.99.65":"b2b2",
          "10.44.20.156":"b2c1",
          "10.171.64.130":"b2c2",
          "10.44.12.47":"oms",
          "10.165.121.122":"system1",
          "10.171.64.30":"system2",
          "10.204.8.12":"user1",
          "10.44.41.53":"user2",
          "10.171.54.126":"dis1",
          "10.172.84.42":"dis2",
          "10.171.127.171":"route1",
          "10.51.74.212":"route2",
          "10.51.73.55":"lvbb1",
          "10.44.13.206":"lvbb2",
          "10.44.9.50":"app"}


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = "ynsymonitor@163.com"
password = "3uQs3ZRXBz"
to_addr = "ynsymonitor@163.com"
smtp_server = "smtp.163.com"


def mailsend(mes):
    msg = MIMEText(mes, 'plain', 'utf-8')
    msg['From'] = _format_addr(u'报警 <%s>' % from_addr)
    msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
    msg['Subject'] = Header(u'阿里服务器', 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 25)
    # server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


def disk(disk_status):
    for i in file.readlines():
        reip = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
        if reip.findall(i):
            disk_ip=reip.findall(i)[0]
            #print reip.findall(i)[0]
        else:
            disk_num=i.split()[-2]
            disk_fenqu=i.split()[-1]
            if disk_num.strip("%").isdigit():
                if int(disk_num.strip("%")) >= 70:
                    disk_status+=disk_num + " " + disk_fenqu + " " + disk_ip+" "+ser_name[disk_ip]+"\n"
    return disk_status

disk_status=disk(disk_status)
#assert disk_status
disk_file=open("disk.pkl",'ab')
if disk_status=="":
    disk_status="磁盘使用正常"
    pickle.dump(disk_status,disk_file)
    disk_file.close()
else:
    mailsend(disk_status)

file.close()









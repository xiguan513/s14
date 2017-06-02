#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time
import sys
import os
import re
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import pickle


work_file='C:\Users\\root\Desktop\Presentation\\%s.txt' % time.strftime('%Y-%m-%d')



from_addr = "ynsymonitor@163.com"
password = "3uQs3ZRXBz"
to_addr = "2851123687@qq.com"
#to_addr = "ynsymonitor@163.com"
smtp_server = "smtp.163.com"

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))


def mailsend(mes):
    msg = MIMEText(mes, 'plain', 'utf-8')
    msg['From'] = _format_addr(u'宋兵 <%s>' % from_addr)
    msg['To'] = _format_addr(u'张莉 <%s>' % to_addr)
    msg['Subject'] = Header(u'宋兵工作日报 %s' % time.strftime('%Y-%m-%d'),'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 25)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()




if __name__=="__main__":
    try:
        work_list=[]
        with open(r'%s' % work_file,'r') as wf:
            for line in wf.readlines():
                line=line.strip('\n')
                work_list.append(line)

        mes='\n'.join(work_list)
        mailsend(mes)
    except IOError as e:
        print e


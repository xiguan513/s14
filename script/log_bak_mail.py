#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import sys


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
    msg['From'] = _format_addr(u'日志备份 <%s>' % from_addr)
    msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
    msg['Subject'] = Header(u'阿里服务器', 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 25)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

mailsend(sys.argv[1])


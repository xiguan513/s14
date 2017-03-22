#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import socket
import os
class FtpClinet(object):
    def __init__(self,host,port):
        self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host,port))

    def start(self):
        self.interactive()

    def interactive(self):
        while True:
            user_input=raw_input(">>").strip()
            if len(user_input)==0:continue
            user_input=user_input.split()

            if hasattr(self,user_input[0]):#判断此类中是否有user_input[0]的方法，此处self表示当前类
                func=getattr(self,user_input[0]) #把此类中user_input[0]的方法主体赋值给func
                func(user_input)#调用次方法
            else:
                print "\033[31;1mWrong cmd usage \033[0m"

    def get(self,msg):
        print "--get func--",msg
        if len(msg)==2:
            file_name=msg[1]
            instrunction="FileTransfer|get|%s" % file_name
            self.sock.send(instrunction)
            feedback=self.sock.recv(1024)
            print "-->",feedback
            if feedback.startswith("FileTransfer|get|ready"):
                file_size=int(feedback.split("|")[-1])
                print "接收文件大小",file_size,type(file_size)
                self.sock.send("FileTransfer|get|recv_ready")
                recv_size=0
                f=file("client_recv/%s" % os.path.basename(file_name),'wb')
                print "--->",file_name
                while not file_size==recv_size:
                    if file_size-recv_size>1024:
                        data=self.sock.recv(1024)
                        recv_size+=len(data)
                        #print "第一个data",len(data)
                        print "下载文件222222222222222222222222222"
                    else:
                        data=self.sock.recv(file_size-recv_size)
                        #print "第二个data",len(data)
                        recv_size+=(file_size-recv_size)
                    #print "第三个data",len(data)
                    f.write(data)
                    print "ceshi"
                    print file_size,recv_size
                else:
                    print "---recv file:%s----" % file_name
                    f.close()
            else:
                print "2222222222222222222222222222222222222222222222"
                print feedback
        else:
            print "\-33[021;1mWrong cmd usage \033[0m"

if __name__=="__main__":
    f=FtpClinet('127.0.0.1',9002)
    f.start()
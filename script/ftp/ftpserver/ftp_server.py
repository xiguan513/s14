#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import SocketServer
import os

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        while True:
            instrunction=self.request.recv(1024).strip() #设置接收信息，并去除空格
            if not instrunction:break   #判断是否为空，如果为空跳出循环
            instrunction=instrunction.split('|') #根据|进行分割字符串
            print "输出分割以后的字符串列表",instrunction
            if hasattr(self,instrunction[0]): #判断类中是否有这个方法
                func=getattr(self,instrunction[0]) #
                func(instrunction)

    def FileTransfer(self,msg):
        print "---filetransfer----",msg
        if msg[1]=='get':
            print "client wants to download file:",msg[2]
            if os.path.isfile(msg[2]):
                file_size=os.path.getsize(msg[2])
                file_size=int(file_size)
                res="ready|%s" % file_size
            else:
                res="file doesn't exist"

            send_confirmation="FileTransfer|get|%s" % res
            self.request.send(send_confirmation)
            feedback=self.request.recv(1024)
            print "准备下载1111111111111111111111111111111"
            if feedback=="FileTransfer|get|recv_ready":
                f=file(msg[2],'rb')
                send_szie=0
                while not file_size==send_szie:
                    print "输出文件大小和发送文件大小",file_size,send_szie
                    print "输出格式",type(file_size),type(send_szie)
                    if file_size-send_szie>1024:
                        data=f.read(1024)
                        send_szie+=1024
                        print "计算文件大于1024的时候文件大小：%s" % send_szie
                    else:
                        print "计算文件111111111111111111111111111"
                        data=f.read(file_size-send_szie)
                        send_szie+=(file_size-send_szie)
                        print "计算文件小于1024的时候文件大小 %s " % send_szie
                    print "发送文件大小：%s " % send_szie
                    self.request.send(data)
                else:
                    print "----send file:%s done-----" % msg[2]
            else:
                print "出错"

if __name__=="__main__":
    HOST,PORT='127.0.0.1',9002
    server=SocketServer.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
    server.serve_forever()

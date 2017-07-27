#!/usr/bin/env python
#-*- coding:utf-8 -*-

import json


""""
{
  "status": "ok",
  "message": "success",
  "datas":[
    {
      "dataNum":"1111111111111111111111111111111111"
    },
    {
      "dataNum":"12222222222222222222222222222222222"
    }
    ]

"""
data = {
    u'status': u'ok',
    u'message': u'success',
    u'datas': [

            ]
        }


with open("1.log") as f:
    num=len(f.readlines())
    line=0
    f.seek(0)

    for  i in f.readlines():
        a={"dataNum" : i}

        data[u"datas"].append(a)


    # for i in f.readlines():
    #     print i

# test_dict = {
#     u'status': u'ok',
#     u'message': u'success',
#     u'datas': [
#
#     ]
# }
# test_dict[u'datas'].append("2017-06-22 15:59:00.223 [org.springframework.scheduling.quartz.SchedulerFactoryBean#0_Worker-6] DEBUG o.h.e.t.i.jdbc.JdbcTransaction - re-enabling autocommit")
with open("2.json","w") as c:
    c.write(json.dumps(data))

#print data



# file_object = open(r"page.json")
# try:
#      all_the_text = file_object.read()
#      print(json.loads(all_the_text))
#      arr = json.loads(all_the_text)
#      for a in arr:
#          print(a)
# finally:
#      file_object.close()
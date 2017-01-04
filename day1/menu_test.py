#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# print("#"*50)
# l=(len(("#"*50)))
# print ("Number:%-50{num} City:%-8{city}".format(num="1",city="ceshi"))
#
# print ("Nmae:%-10s Age:%-8d Height:%-8.2f" %("Aviad",25,1.83))
#
#
# for i in range(0,2):
#     print(i)


china={"BeiJing":{"HaiDianQu":{"ZhongGuanCun":"No. 11"},
                  "ChaoYangQu":{"SanYuanQiao":"No. 12"}},
       "Shanghai":{"PuDongQu":{"Airport":"No. 21"},
                   "BaoShanQu":{"JiangWanZhen":"No. 31"}},
       "HeNanSheng":{"XuChang":{"Park":"No. 31"},
                     "ZhengZhou":{"ChangJiangLu":"NO. 201"}},
       }

print(china)

print("==================")
print(china["BeiJing"])
for i in china["BeiJing"]:
    print(i)
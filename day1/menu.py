#!/usr/bin/env python
# -*- coding: UTF-8 -*-

china={"BeiJing":{"HaiDianQu":{"ZhongGuanCun":"No. 11"},
                  "ChaoYangQu":{"SanYuanQiao":"No. 12"}},
       "Shanghai":{"PuDongQu":{"Airport":"No. 21"},
                   "BaoShanQu":{"JiangWanZhen":"No. 31"}},
       "HeNanSheng":{"XuChang":{"Park":"No. 31"},
                     "ZhengZhou":{"ChangJiangLu":"NO. 201"}},
       }

#print(china["BeiJing"]["HaiDianQu"]["ZhongGuanCun"])

print("显示现有的城市：")
print("#"*60)

while True:
    city_list = []
    go_list = []
    for num, city in enumerate(china):
        print("Number:%-35d City:%-2s" % (num, city), end="\n")
        city_list.append(city)
    print("Number:%-35s Qi:%-2s" % ("e", "exit"), end="\n")
    while True:
        try:
            go_city=input("Please enter the city number you are going to： ")
            if go_city.isdigit():
                go_city=int(go_city)
            elif go_city=="e":
                break
            for k,i in enumerate(china[city_list[go_city]]):
                print(k,i)

        except IndexError:
            print("Please enter the correct city number")



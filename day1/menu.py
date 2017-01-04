#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
    三级菜单
    可依次选择进入各子菜单
    所需知识点: 列表，字典
"""



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
    go1_list = []
    go2_list = []
    for num, city in enumerate(china):
        print("Number:%-35d City:%-2s" % (num, city), end="\n")
        city_list.append(city)
    print("Number:%-35s Qi:%-2s" % ("e", "exit"), end="\n")
    while True:
        try:#异常检测
            go_city=input("Please enter the city number you are going to： ")
            if go_city.isdigit():
                go_city=int(go_city)
            elif go_city=="e":
                break
            for k,i in enumerate(china[city_list[go_city]]):#通过字典取值
                print(k,i)
                go1_list.append(i)
            go1_city=int(input("Please input your number: "))
            for k,i in enumerate(china[city_list[go_city]][go1_list[go1_city]]):
                print(k,i)
                go2_list.append(i)
            go2_city=int(input("Please inpur your number: "))
            for i in china[city_list[go_city]][go1_list[go1_city]][go2_list[go2_city]]:
                print(i,end="")
            else:
                print("\n")

        except IndexError:
            print("Please enter the correct city number")



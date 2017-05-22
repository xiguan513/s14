#!/usrs/bin/evn python
# -*- coding:utf-8 -*-

import xlsxwriter

work=xlsxwriter.Workbook("图表.xlsx")
workseet=work.add_worksheet("int")

title_index=["A","B","C","D","E","F"]
title=["int","for","while","range","mk","测试"]
data=[20,30,50,90,64,75]

#创建字体加粗格式
bold=work.add_format({"bold":True})
for i,j in enumerate(title_index):
    point="%s%s" % (j,2)
    content=data[i]
    workseet.write(point,content)

for i,j in enumerate(title_index):
    point="%s%s" % (j,1)
    content=title[i]
    workseet.write(point,content,bold)

#column柱状图
#area面积图
#bar条形图
#line折线图
#radar雷达图



chart=work.add_chart({"type":"bar"})#创建一个柱状图
chart.add_series(
    {
        "categories":"=int!$A$1:$F$1",#类别标签的范围
        "values":"=int!$A$2:$F$2",#图表数据的范围
        "line":{"color":"red"}#图表线条的属性
    }
)
workseet.insert_chart("A4",chart)
work.close()

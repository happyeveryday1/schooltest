#coding=utf-8
#导入函数
import csv

my_files="E:\\mywork\\9_4.csv"
data=csv.reader(file(my_files,'rb'),'gb2312')
for user in data:
    print user[0]
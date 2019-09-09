# *_*coding:utf-8 *_*
import os
path='E:\\mywork\\schooltest\\test_case\\'
caselist=os.listdir(path) #获取指定目录中的内容
for a in caselist:
    s=a.split('.')[1] #选取后缀名为 py 的文件
    if s=='py': #此处执行 dos 命令并将结果保存到 log.txt
        os.system('E:\\mywork\\schooltest\\test_case\\%s 1>>log.txt 2>&1'%a)
# *_*coding:utf-8 *_*
import os,datetime,time
result_dir = 'E:\\mywork\\schooltest\\report'
lists=os.listdir(result_dir)
lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not
os.path.isdir(result_dir+"\\"+fn) else 0)
print ('最新的文件为： '+lists[-1])
file = os.path.join(result_dir,lists[-2])
print file
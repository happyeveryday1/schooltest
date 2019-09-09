# *_*coding:utf-8 *_*
import sys
sys.path.append('...')
from test_case import start_baidu,start_ddc
#用例文件列表
def caselist():
    alltestnames = [
        start_baidu.Baidu,
        start_ddc.System
    ]
    print "success read case list"
    return alltestnames
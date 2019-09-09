# *_*coding:utf-8 *_*
import unittest
import time
import allcase_list
import HTMLTestRunner
#这里需要导入测试文件

from test_case import start_baidu,start_ddc

listaa='E:\\mywork\\schooltest\\test_case'
def creatsuite1():
    testunit = unittest.TestSuite()
    # 将测试用例加入到测试容器(套件)中

    # discover 方法定义
    discover = unittest.defaultTestLoader.discover(listaa,
                                                   pattern='start_*.py',
                                                   top_level_dir=None)

    # discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print testunit
    return testunit

alltestnames=creatsuite1()

#执行测试套件
#runner = unittest.TextTestRunner()
#runner.run(testunit)
now = time.strftime("%Y-%m-%d %H-%M-%S",time.localtime())
filename = 'E:\\mywork\\schooltest\\report\\'+now+'result2.html'
fp= file(filename, 'wb')
    # 定义测试报告d
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'测试报告',
    description=u'用例执行情况：')
# 运行测试用例
runner.run(alltestnames)
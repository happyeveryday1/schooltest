# *_*coding:utf-8 *_*
from selenium import webdriver
import unittest
import HTMLTestRunner
import sys
import time
sys.path.append('..')
from test_case.public import login
from test_case.public import quit


#导入登录文件

class System(unittest.TestCase):
    def setUp(self) :
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get("http://192.168.1.100/")
        self.verificationErrors = []  #脚步运行时，错误的信息将被打印到这个表中
        self.accept_next_alert = True  #是否接受下一个警告


    #登录用例
    def test_login(self):
        u"""ddc登录"""
        driver=self.driver
        #调用登录模块
        login.login(self)
        time.sleep(2)
        quit.quit(self)

    #修改ddc名称
    '''def test_ddc_name_modify(self):
        driver=self.driver
        driver.find_element_by_name("NAME").clear()
        driver.find_element_by_name("NAME").send_keys("DDC4")
        driver.find_element_by_xpath('/html/body/div[2]/form[1]/div[2]/button').click()
        reload(sys)
        sys.setdefaultencoding('utf8')
        if driver.find_element_by_class_name('alert').text == '成功':
            print "修改DDC命名成功"

    #修改ddcID
    def test_ddc_ID_modify(self):
        driver=self.driver
        driver.find_element_by_name('ID').clear()
        driver.find_element_by_name('ID').send_keys('009569B4669A')
        driver.find_element_by_xpath('/html/body/div[2]/form[2]/div[2]/button').click()
        if driver.find_element_by_xpath('/html/body/div[2]/div').text == 'OK 重启生效':
            print "修改id成功"

    # 同步时间
    def test_synchronizing_time(self):
        driver=self.driver
        driver.find_element_by_xpath('/html/body/div[2]/form[3]/div[2]/button').click()
        if driver.find_element_by_xpath('/html/body/div[2]/div').text == '成功':
            if driver.find_element_by_xpath('/html/body/div[2]/form[3]/div[1]/div') == time.strftime(
                    '%Y-%m-%d %H:%M:%S', time.localtime(time.time())):
                print "同步时间成功"
            else:
                print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        else:
            print "同步未成功"

    #查找ddc
    def test_find_ddc(self):
        driver=self.driver
        driver.find_element_by_xpath('/html/body/div[2]/form[4]/div/a').click()
        if driver.find_element_by_xpath('/html/body/div[2]/div').text == '成功':
            print "查找成功"
            '''


    def tearDown(self):
        self.driver.quit()
        #对前面 verificationErrors 方法获得的列表进行比较；
        # 如查 verificationErrors 的列表不为空，输出列表中的报错信息。
        self.assertEqual([], self.verificationErrors)

if __name__=="__main__":
    # 定义一个单元测试容器
    testunit = unittest.TestSuite()
    # 将测试用例加入到测试容器中
    testunit.addTest(System("test_login"))
    #testunit.addTest(System("test_ddc_name_modify"))
    # 定义个报告存放路径，支持相对路径
    filename = 'E:\\mywork\\schooltest\\report\\result.html'
    fp = file(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'ddc系统设置',
        description=u'用例执行情况：')
    # 运行测试用例
    runner.run(testunit)


# *_*coding:utf-8 *_*
#-*-coding=utf-8
from selenium import webdriver
import sys
import os,time
import requests

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\'}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(chrome_options=options)


driver.get('http://192.168.1.100')
time.sleep(2)
driver.maximize_window()
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys("root")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("www.lierda.com")
driver.find_element_by_class_name("btn").click()
time.sleep(1)
'''driver.find_element_by_link_text('设置').click()
driver.find_element_by_link_text('系统设置').click()
#修改ddc
driver.find_element_by_name("NAME").clear()
driver.find_element_by_name("NAME").send_keys("DDC4")
driver.find_element_by_xpath('/html/body/div[2]/form[1]/div[2]/button').click()
reload(sys)
sys.setdefaultencoding('utf8')
if driver.find_element_by_class_name('alert').text=='成功':
    print "修改DDC命名成功"


#修改ddcID
driver.find_element_by_name('ID').clear()
driver.find_element_by_name('ID').send_keys('009569B4669A')
driver.find_element_by_xpath('/html/body/div[2]/form[2]/div[2]/button').click()
if driver.find_element_by_xpath('/html/body/div[2]/div').text=='OK 重启生效':
    print "修改id成功"

#同步时间
driver.find_element_by_xpath('/html/body/div[2]/form[3]/div[2]/button').click()
if driver.find_element_by_xpath('/html/body/div[2]/div').text=='成功':
    if driver.find_element_by_xpath('/html/body/div[2]/form[3]/div[1]/div')==time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())):
        print "同步时间成功"
    else:
        print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

else:
    print "同步未成功"


#查找ddc
driver.find_element_by_xpath('/html/body/div[2]/form[4]/div/a').click()
if driver.find_element_by_xpath('/html/body/div[2]/div').text=='成功':
    print "查找成功"


#导出配置
driver.find_element_by_xpath('/html/body/div[2]/form[5]/div/button').click()
time.sleep(3)

#恢复配置
driver.find_element_by_name("backup").send_keys('D:\\ddc3_backup.bin')
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/form[6]/div/div[2]/button').click()
time.sleep(3)

#修改密码
driver.find_element_by_name('old_password').send_keys('www.lierda.com')
driver.find_element_by_name('new_password').send_keys('www.lierda.com')
driver.find_element_by_name('repeat_password').send_keys('www.lierda.com')
driver.find_element_by_xpath('/html/body/div[2]/form[7]/div[4]/button').click()
try:
    picture_url=driver.get_screenshot_as_file('E:\\mywork\\schooltest\\picture\\changepassword.png')
    print("%s：截图成功！！！，密码修改成功" % picture_url)
except BaseException as msg:
    print(msg)
time.sleep(2)'''

#网络设置
driver.find_element_by_link_text('设置').click()
driver.find_element_by_link_text('网络设置').click()
#外网连接检查
driver.find_element_by_xpath('/html/body/div[2]/form[1]/div/a').click()
try:
    picture_url=driver.get_screenshot_as_file('E:\\mywork\\schooltest\\picture\\network.png')
    print("%s：截图成功！！！,网络连接OK" % picture_url)
except BaseException as msg:
    print(msg)
time.sleep(2)

#网络
driver.find_element_by_name('NETWORK_TYPE').find_element_by_xpath('/html/body/div[2]/form[2]/div[1]/div/select/option[2]').click()
driver.find_element_by_xpath('/html/body/div[2]/form[2]/div[6]/button').click()
try:
    picture_url=driver.get_screenshot_as_file('E:\\mywork\\schooltest\\picture\\networksetting.png')
    print("%s：截图成功！！！,网络设置已经生效" % picture_url)
except BaseException as msg:
    print(msg)

#服务器设置
driver.find_element_by_name('JSON_SERVER_IP').clear()
driver.find_element_by_name('JSON_SERVER_IP').send_keys('test.lierdalux.cn')
driver.find_element_by_name('JSON_SERVER_PORT').clear()
driver.find_element_by_name('JSON_SERVER_PORT').send_keys('9000')
driver.find_element_by_xpath('/html/body/div[2]/form[3]/div[4]/button').click()
try:
    picture_url=driver.get_screenshot_as_file('E:\\mywork\\schooltest\\picture\\service_setting.png')
    print("%s：截图成功！！！" % picture_url)
except BaseException as msg:
    print(msg)

driver.find_element_by_xpath('/html/body/div[2]/form[4]/div/button').click()

time.sleep(2)
driver.quit()
# *_*coding:utf-8 *_*

from selenium import webdriver
from time import sleep
import time

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\'}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(chrome_options=options)
driver.get('http://192.168.100.1')
time.sleep(2)
driver.maximize_window()
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys("root")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("www.lierda.com")
driver.find_element_by_class_name("btn").click()
driver.find_element_by_link_text('设置').click()
driver.find_element_by_link_text('系统设置').click()
driver.find_element_by_xpath('/html/body/div[2]/form[5]/div/button').click()
sleep(3)
driver.quit()

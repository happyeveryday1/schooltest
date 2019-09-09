#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time,unittest


#登录模块
def login(self):
    driver=self.driver
    driver.maximize_window()
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys("root")
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys("www.lierda.com")
    driver.find_element_by_class_name("btn").click()
    time.sleep(3)

    texts=driver.find_element_by_xpath('/html/body/div[2]/div/dl[1]/dd[1]').text
    if texts=="3.12.0":
        print "ddc版本正确"
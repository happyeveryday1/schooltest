# *_*coding:utf-8 *_*
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time,unittest

def setting(self):
    driver.find_element_by_link_text('设置').find_elements_by_link_text("系统设置").click()
    time.sleep(3)
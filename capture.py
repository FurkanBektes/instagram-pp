#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def screenshot():
	driver.get_screenshot_as_file(img)
	time.sleep(2)
	screenshot()

options = Options()
options.add_argument("--headless")
options.add_argument('--disable-gpu')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(executable_path='Your chrome path', chrome_options=options) # like '/Users/xxxx/Desktop/chromedriver'

getDriver = ("http://www.clocktab.com/")

img = "webshot.png"

driver.set_window_position(0, 0)
driver.set_window_size(1500, 1000)

try:
	driver.get(getDriver)
	time.sleep(4)
	Select(driver.find_element_by_id('theme')).select_by_value('simple')
	#driver.find_element_by_xpath("//input[@id='bg']").send_keys('black')
	driver.find_element_by_id('12_hour').click()
	screenshot()
except:
    print("Connection NOT Established. Please check your network")

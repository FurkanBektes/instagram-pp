#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException

username = 'xxxxx'
password = 'xxxxx'

def change():
	#driver.find_element_by_xpath("//button[contains(.,'Change Profile Photo')]").click()
	driver.find_element_by_xpath("//button[contains(.,'Modifier la photo de profil')]").click()
	driver.find_element_by_xpath("//input[@class='tb_sK']").send_keys("webshot.png")
	#driver.find_element_by_xpath("//button[contains(.,'Cancel')]").click()
	driver.find_element_by_xpath("//button[contains(.,'Annuler')]").click()
	driver.refresh()
	change()
	
options = Options()
options.add_argument("--headless")
options.add_argument('--disable-gpu')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(executable_path='Your chrome path', chrome_options=options) # like '/Users/xxxx/Desktop/chromedriver'

getDriver = ("https://www.instagram.com/accounts/edit/")
try:
    driver.get(getDriver)
    time.sleep(4)
    
    #driver.find_element_by_class_name('hztqj').click()
    #Select(driver.find_element_by_class_name('hztqj')).select_by_value('en')
    #time.sleep(4)

    #driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
    #driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    #driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()
    
    driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    driver.find_element_by_xpath("//button[contains(.,'Connexion')]").click()
    print("Connection Established to your instagram")
    print("Profile picture are changing")
    time.sleep(4)
    change()
except:
    print("Connection NOT Established. Please check your network")
    time.sleep(600)
    change()

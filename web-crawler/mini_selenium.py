#! /usr/bin/python3

import os
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
binary = FirefoxBinary(r'D:\Program Files (x86)\Mozilla Firefox\firefox.exe')
browser = webdriver.Firefox(firefox_binary=binary, executable_path=gecko+'.exe')

print(type(browser))

browser.get('http://inventwithpyhton.com')
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Cedar
# @Date  : 2021/4/13
# @Desc  :


from selenium import webdriver
import time


options = webdriver.ChromeOptions()
options.add_experimental_option('androidPackage', 'com.android.chrome')
options.add_experimental_option('androidUseRunningApp', True)
options.add_experimental_option('androidProcess', 'com.android.chrome')
# options.add_experimental_option('androidDeviceSerial', 'SM_G977N')
# options.add_experimental_option('androidActivity', 'com.google.android.apps.chrome.Main')


driver = webdriver.Chrome('./chromedriver_dir/chromedriver_90.exe', options=options)
# driver.get('https://m.facebook.com/benger.won')
driver.get('https://m.facebook.com/nba')
time.sleep(3)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

page_html = driver.page_source
print(page_html)

driver.quit()

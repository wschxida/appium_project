#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Cedar
# @Date  : 2021/4/13
# @Desc  :


from selenium import webdriver
options = webdriver.ChromeOptions()
# options.add_experimental_option('androidPackage', 'com.android.chrome')
driver = webdriver.Chrome('./chromedriver_dir/chromedriver_90.exe', options=options)
driver.get('https://m.facebook.com/benger.won')

page_html = driver.page_source
print(page_html)

driver.quit()

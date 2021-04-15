#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Cedar
# @Date  : 2021/4/13
# @Desc  :


from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('androidPackage', 'com.android.chrome')
# options.add_argument(r'user-data-dir=E:\python_project\appium_project\service\model\chrome\user_data_1')
driver = webdriver.Chrome('./chromedriver_dir/chromedriver_89.exe', options=options)
driver.get('https://m.facebook.com/benger.won')
driver.quit()

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import base64
import logging
import os


# 日志记录
logger = logging.getLogger()
logger.setLevel('INFO')

BASIC_FORMAT = "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter(BASIC_FORMAT, DATE_FORMAT)

# logFile = 'twitter_get_guest_token.log'
# fl_handler = RotatingFileHandler(logFile, mode='a', maxBytes=5*1024*1024, backupCount=2, encoding='utf-8', delay=0)
# fl_handler.setFormatter(formatter)

stream = logging.StreamHandler()  # 输出到控制台的handler
stream.setFormatter(formatter)
stream.setLevel('INFO')

# logger.addHandler(fl_handler)
logger.addHandler(stream)

cur_path = os.path.dirname(os.path.realpath(__file__))
cfg_path = os.path.join(cur_path, '..', "config.ini")  # 读取到本机的配置文件


def start_appium():
    # 模拟器
    # desired_caps = {
    #     'platformName': 'Android',
    #     'deviceName': 'yeshen',
    #     'appPackage': 'com.android.chrome',
    #     'appActivity': 'com.google.android.apps.chrome.Main',
    #     'platformVersion': '7',
    #     'newCommandTimeout': 6000,
    #     'noReset': True,
    #     'unicodeKeyboard': True,
    #     'autoGrantPermissions': True,
    #     'resetKeyboard': True,
    #     'fullReset': False,
    #     # 直接指定浏览器名称参数为chrome【重点添加了这一步】
    #     # 'browserName': 'chrome',
    #     # 使用指定的浏览器驱动-匹配手机上的谷歌浏览器
    #     'chromedriverExecutable': r'E:/python_project/appium_project/service/model/chromedriver_dir/chromedriver_89.exe'
    # }

    # 手机
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Redmi_Note_7',
        'appPackage': 'com.android.chrome',
        'appActivity': 'com.google.android.apps.chrome.Main',
        'platformVersion': '10',
        'newCommandTimeout': 6000,
        'noReset': True,
        'unicodeKeyboard': True,
        'autoGrantPermissions': True,
        'resetKeyboard': True,
        'fullReset': False,
        'chromedriverExecutable': r'E:/python_project/appium_project/service/model/chromedriver_dir/chromedriver_81.exe'
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    driver.implicitly_wait(10)

    driver.get('https://m.facebook.com/benger.won')
    time.sleep(2)
    # 屏幕宽
    width = driver.get_window_size()['width']
    # 屏幕高
    height = driver.get_window_size()['height']
    # 滑动
    for i in range(2):
        driver.swipe(width * 0.5, height * 0.9, width * 0.5, height * 0.1, 1000)
        WebDriverWait(driver, 3)
        time.sleep(1)

    # # 查看context的名称
    # print(driver.contexts)
    # # 当前处于哪个context?
    # print(driver.current_context)
    #
    # driver.switch_to.context('WEBVIEW_chrome')
    # print(driver.current_context)
    contexts = driver.contexts
    print(contexts)
    driver.switch_to.context(contexts[1])

    # driver.find_element_by_xpath('.//*[@content-desc="网页视图"]').click()
    # 获取页面html，并保存到本地
    page_html = driver.page_source
    print(page_html)

    # 退出
    driver.quit()


if __name__ == '__main__':
    start_appium()


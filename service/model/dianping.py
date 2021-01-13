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
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'yeshen',
        'appPackage': 'com.dianping.v1',
        'appActivity': 'com.dianping.channel.food.ShopListFoodActivity',
        'platformVersion': '7',
        'newCommandTimeout': 6000,
        'noReset': True,
        'unicodeKeyboard': True,
        'autoGrantPermissions': True,
        'resetKeyboard': True,
        'fullReset': False
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    driver.implicitly_wait(10)
    time.sleep(10)

    # 滑动采集
    for i in range(10):

        try:
            item_list = driver.find_elements_by_xpath(
                '//*[@resource-id="com.dianping.v1:id/pagecontainer_recyclerview"]//*[@resource-id="com.dianping.v1:id/shop_item"]')
            print(item_list)
            for item in item_list:
                try:
                    tv_shop_title = item.find_element_by_xpath(
                        './/*[@resource-id="com.dianping.v1:id/tv_shop_title"]').get_attribute('text')
                    tv_shop_price = item.find_element_by_xpath(
                        './/*[@resource-id="com.dianping.v1:id/tv_shop_price"]').get_attribute('text')

                    print(tv_shop_title, tv_shop_price)
                except Exception as e:
                    print(e)

        except Exception as e:
            print(e)

        # 屏幕宽
        width = driver.get_window_size()['width']
        # 屏幕高
        height = driver.get_window_size()['height']
        driver.swipe(width*0.5, height*0.9, width*0.5, height*0.1, 1000)
        WebDriverWait(driver, 3)


if __name__ == '__main__':
    start_appium()


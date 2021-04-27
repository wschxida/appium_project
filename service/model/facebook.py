from appium import webdriver
from selenium import webdriver as sele_webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def start_appium():
    # # 雷电模拟器
    # desired_caps = {
    #     'platformName': 'Android',
    #     'deviceName': 'emulator-5554',
    #     'appPackage': 'com.tencent.mtt.x86',
    #     'appActivity': '.MainActivity',
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

    # # 夜神
    # desired_caps = {
    #     'platformName': 'Android',
    #     'deviceName': 'SM_G977N',
    #     'appPackage': 'com.android.chrome',
    #     'appActivity': 'com.google.android.apps.chrome.Main',
    #     'platformVersion': '4',
    #     'newCommandTimeout': 6000,
    #     'noReset': True,
    #     'unicodeKeyboard': True,
    #     'autoGrantPermissions': True,
    #     'resetKeyboard': True,
    #     'fullReset': False,
    #     # 直接指定浏览器名称参数为chrome【重点添加了这一步】
    #     # 'browserName': 'Chrome',
    #     # 使用指定的浏览器驱动-匹配手机上的谷歌浏览器
    #     'chromedriverExecutable': r'E:/python_project/appium_project/service/model/chromedriver_dir/chromedriver_90.exe'
    # }

    # # 手机
    # desired_caps = {
    #     'platformName': 'Android',
    #     'deviceName': 'Redmi_Note_7',
    #     'appPackage': 'com.android.chrome',
    #     'appActivity': 'com.google.android.apps.chrome.Main',
    #     # 'appPackage': 'com.facebook.katana',
    #     # 'appActivity': '.activity.FbMainTabActivity',
    #     'platformVersion': '10',
    #     'newCommandTimeout': 6000,
    #     'noReset': True,
    #     'unicodeKeyboard': True,
    #     'autoGrantPermissions': True,
    #     'resetKeyboard': True,
    #     'fullReset': False,
    #     'chromedriverExecutable': r'E:/python_project/page_agent_queue_service/cloud_service/chromedriver_dir/chromedriver_81.exe'
    # }

    # 逍遥
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'VOG-AL00',
        'appPackage': 'com.android.browser',
        'appActivity': '.BrowserActivity',
        'platformVersion': '7',
        'newCommandTimeout': 6000,
        'noReset': True,
        'unicodeKeyboard': True,
        'autoGrantPermissions': True,
        'resetKeyboard': True,
        'fullReset': False,
        # 直接指定浏览器名称参数为chrome【重点添加了这一步】
        # 'browserName': 'Chrome',
        # 使用指定的浏览器驱动-匹配手机上的谷歌浏览器
        # 'chromedriverExecutable': r'E:/python_project/appium_project/service/model/chromedriver_dir/chromedriver_90.exe'
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    driver.implicitly_wait(10)

    driver.get("https://www.facebook.com/bbc")
    # driver.get("http://m.sohu.com/")
    time.sleep(5)
    # # 输入字段
    # driver.find_element_by_xpath('.//*[@text="Search Search"]').click()
    # time.sleep(1)
    # driver.find_element_by_xpath('.//*[@resource-id="main-search-input"]').send_keys("https://www.facebook.com/guosha.san")
    # driver.press_keycode(66)  # 回车
    # time.sleep(3)
    #
    # # 屏幕宽
    # width = driver.get_window_size()['width']
    # # 屏幕高
    # height = driver.get_window_size()['height']
    #
    # print(width, height)
    # x1 = int(0.37 * width)
    # y1 = int(0.4 * height)
    # print(x1, y1)
    # driver.tap([(x1, y1)], 0)
    # time.sleep(5)

    # 屏幕宽
    width = driver.get_window_size()['width']
    # 屏幕高
    height = driver.get_window_size()['height']
    for i in range(3):
        driver.swipe(width * 0.5, height * 0.9, width * 0.5, height * 0.1, 1000)
        WebDriverWait(driver, 2)

    contexts = driver.contexts
    print(contexts)
    driver.switch_to.context(contexts[1])
    time.sleep(10)

    # 获取页面html，并保存到本地
    page_html = driver.page_source
    print(page_html)

    # 退出
    driver.quit()


if __name__ == '__main__':
    start_appium()


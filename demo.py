import time
from appium import webdriver

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

# 获取toast
desired_caps['automationName'] = 'Uiautomator2'

# 默认不重置
desired_caps['noReset'] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


# 1.通过滑动4次找设置中的 关于手机 并点击
# for i in range(4):
#     driver.swipe(100, 2000, 100, 1000, 1000)
#
# driver.find_element_by_xpath("//*[@text='关于手机']").click()

# 2.先找，如果有，直接定位，如果没有再滑动
for i in range(10):
    try:
        driver.find_element_by_xpath("//*[@text='应用']").click()
        break
    except Exception:
        driver.swipe(100, 2000, 100, 1000, 1000)









time.sleep(5)
driver.quit()
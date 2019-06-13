from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):

    # 按钮 我
    me_feature = By.XPATH, "//*[@text='我']"


    # 点击按钮 我
    def click_me(self):
        self.click(self.me_feature)

    # 如果没有登录就登录 com.yunmall.ymctoc.ui.activity.MainActivity
    def login_if_not(self, page):
        self.click_me()

        # 如果没有登录就登录
        if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.MainActivity":
            page.register.click_to_login()
            page.login.input_username("itheima_test")
            page.login.input_password("itheima")
            page.login.click_login_btn()
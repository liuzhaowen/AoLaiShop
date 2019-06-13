from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):

    # 按钮 我
    me_feature = By.XPATH, "//*[@text='我']"


    # 点击按钮 我
    def click_me(self):
        self.click(self.me_feature)
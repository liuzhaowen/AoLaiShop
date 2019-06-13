from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class RegisterPage(BaseAction):

    # 已有账号，去登录
    to_login_feature = By.XPATH, "//*[@text='已有账号，去登录']"

    # 点击 已有账号，去登录
    def click_to_login(self):
        self.click(self.to_login_feature)

    
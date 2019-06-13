from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):

    # 账号输入框
    username_feature = By.ID, "com.yunmall.lc:id/logon_account_textview"

    # 密码输入框
    password_feature = By.ID, "com.yunmall.lc:id/logon_password_textview"

    # 登录按钮
    login_btn_feature = By.ID, "com.yunmall.lc:id/logon_button"

    # 输入用户名
    def input_username(self, username):
        self.input(self.username_feature, username)

    # 输入用户密码
    def input_password(self, password):
        self.input(self.password_feature, password)

    # 点击登录按钮
    def click_login_btn(self):
        self.click(self.login_btn_feature)
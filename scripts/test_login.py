import time

from base.base_driver import init_driver
from page.page import Page


class TestLogin:


    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()


    def test_login(self):

        # 在home页点击me
        self.page.home.click_me()
        # 在register页点击 已有账号去登录
        self.page.register.click_to_login()
        # 在login页输入用户名
        self.page.login.input_username("itheima_test")
        # 在login页输入密码
        self.page.login.input_password("itheima")
        # 在login页点击登录按钮
        self.page.login.click_login_btn()
        # 在me 页获取个人信息页断言
        assert "itheima_test" == self.page.me.get_nickname()
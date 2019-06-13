import time

import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestLogin:


    def setup(self):
        self.driver = init_driver(False)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()


    @pytest.mark.parametrize("args", analyze_file("login_data.yaml", "test_login"))
    def test_login(self, args):

        username = args["username"]
        password = args["password"]
        toast = args["toast"]

        # 在home页点击me
        self.page.home.click_me()
        # 在register页点击 已有账号去登录
        self.page.register.click_to_login()
        # 在login页输入用户名
        self.page.login.input_username(username)
        # 在login页输入密码
        self.page.login.input_password(password)
        # 在login页点击登录按钮
        self.page.login.click_login_btn()
        # 根据参数toast 的取值进行断言,toast为None去获取me页面的昵称和用户名比对，否则对判断toast是否存在进行断言
        if toast == None:
            assert "itheima_test" == self.page.me.get_nickname()
        else:
            assert self.page.login.is_toast_exist(toast)
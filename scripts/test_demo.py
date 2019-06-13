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


    def test_demo(self):
        self.page.home.login_if_not(self.page)


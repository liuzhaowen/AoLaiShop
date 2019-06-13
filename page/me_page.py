from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MePage(BaseAction):

    # 昵称
    nickname_feature = By.ID, "com.yunmall.lc:id/tv_user_nikename"

    # 获取昵称
    def get_nickname(self):
        return self.get_text(self.nickname_feature)
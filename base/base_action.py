from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=1.0):
        by = feature[0]
        value = feature[1]

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))

    def find_elements(self, feature, timeout=10, poll=1):
        by = feature[0]
        value = feature[1]

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))

    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, text):
        self.find_element(feature).send_keys(text)

    def get_text(self, feature):
        return self.find_element(feature).text

    # 根据部分toast文本内容判断toast是否存在
    def is_toast_exist(self, text):
        toast_feature = By.XPATH, "//*[contains(@text, '%s')]" % text
        try:
            self.find_element(toast_feature, 10, 0.1)
            return True
        except TimeoutException as e:
            return False

    # 根据部分toast文本内容获取全部toast文本内容
    def get_toast_text(self, text):
        if self.is_toast_exist(text):
            toast_feature = By.XPATH, "//*[contains(@text, '%s')]" % text
            return self.find_element(toast_feature, 5, 0.1).text
        else:
            raise Exception("不好意思，toast信息不存在，请检查参数是否正确或者toast是否出现")

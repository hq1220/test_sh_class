from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def click(self, loc):
        self.find_element(loc).click()

    def input_text(self, loc, text):
        self.find_element(loc).send_keys(text)

    def find_element(self, loc):
        by = loc[0]
        value = loc[1]  # "text,0"
        if by == By.XPATH:
            value = self.make_xpath_with_feature(value)  # //*

        # 加入WebDriverWait的意义:如果第一次没有找到元素,再给点时间找一次
        return WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element(by, value))

    def find_elements(self, loc):
        by = loc[0]
        value = loc[1]
        if by == By.XPATH:
            value = self.make_xpath_with_feature(value)  # //*

        # 加入WebDriverWait的意义:如果第一次没有找到元素,再给点时间找一次
        return WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element(by, value))

    def make_xpath_with_unit_feature(self, loc):
        '''
        拼接xpath中间的部分
        :param loc:
        :return:
        '''
        key_index = 0
        value_index = 1
        option_index = 2

        args = loc.split(",")
        feature = ""

        if len(args) == 2:
            feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and"
        elif len(args) == 3:
            if args[option_index] == "1":
                feature = "@" + args[key_index] + "='" + args[value_index] + "'" + "and"
            elif args[option_index] == "0":
                feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and"

        return feature

    def make_xpath_with_feature(self, loc):
        feature_start = "//*["
        feature_end = "]"
        feature = ""

        if isinstance(loc, str):
            # 如果是正常的xpath
            if loc.startswith("//"):
                return loc

            # loc是一个字符串的情况
            feature = self.make_xpath_with_unit_feature(loc)
        else:
            # loc是一个列表的情况
            for i in loc:
                feature += self.make_xpath_with_unit_feature(i)

        feature = feature.rstrip("and")

        loc = feature_start + feature + feature_end

        return loc

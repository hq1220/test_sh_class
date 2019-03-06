# PO模式概述:测试页面和测试脚本分离，即页面封装成类，供测试脚本进行调用。

# 解决 No module named 'base' 报错
import os, sys

sys.path.append(os.getcwd())

from appium import webdriver
from base.base_driver import init_driver
from page.display_page import DisplayPage


class TestDisplay:

    def setup(self):
        # 这里面的self.driver就相当于接收了来自另外一个文件(base_driver)的前置代码
        self.driver = init_driver()
        # 这里面的self.display_page就相当于新建了一个来自DisplayPage的对象
        self.display_page = DisplayPage(self.driver)

    def test_mobile_display_input(self):
        # 点击放大镜
        self.display_page.click_search()
        # 输入文字
        self.display_page.input_search_text("1")
        # 点击返回
        self.display_page.click_back()

    # def test_wallpaper(self):
    #     self.display_page.click_wallpaper()
    #     self.display_page.click_xxx()

    # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
    # self.driver.find_element_by_id("com.android.settings:id/search").click()
    # self.driver.find_element_by_id("android:id/search_src_text").send_keys("hello")
    # self.driver.find_element_by_class_name("android.widget.ImageButton").click()

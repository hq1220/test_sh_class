# 写page的好处:如果遇到页面里面的东西改了(比如元素的id名称变了等),去修改page相应的代码即可
# 如果是测试流程变化了(比如先点击后返回,改成:先返回后点击),去修改脚本(以test开头的py文件)即可
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class DisplayPage(BaseAction):
    # 显示按钮,这样写实际上是接收了一个元祖
    display_button = By.XPATH, "//*[contains(@text,'显示')]"
    # 搜索按钮
    search_button = By.ID, "com.android.settings:id/search"
    # 搜索框
    input_text_view = By.ID, "android:id/search_src_text"
    # 返回按钮
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    # 继承也可以写init，这叫重写父类方法,如果不需要重写就可以不写了
    # def __init__(self, driver):
    #     # 父类(BaseAction)init方法都有哪些参数,这里就该有哪些参数,不然会报错
    #     BaseAction.__init__(self, driver)
    #     # 点击显示(init 里面可以去写已经确定的这个模块所有的前置功能)
    #     self.click_display()

    def click_display(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        # 等价于下面:
        # self.driver.find_element(self.display_button[0], self.display_button[1]).click()

        # self.find_element(self.display_button).click()

        self.click(self.display_button)

    def click_search(self):
        # self.driver.find_element_by_id("com.android.settings:id/search").click()
        # self.find_element(self.search_button).click()

        self.click(self.search_button)

    def input_search_text(self, text):
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys(text)
        # self.find_element(self.input_text_view).send_keys(text)

        self.input_text(self.input_text_view, text)

    def click_text_view(self):
        # self.driver.find_element(self.input_text_view).click()

        self.click(self.input_text_view)

    def click_back(self):
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        # self.find_element(self.back_button).click()

        self.click(self.back_button)

import os

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from config.setting import DRIVER_DIR

CHROME_PATH = os.path.join(DRIVER_DIR, 'chromedriver.exe')     # 谷歌驱动文件路径
EDGE_PATH = os.path.join(DRIVER_DIR, 'MicrosoftWebDriver.exe')     # EDGE驱动文件路径
FIRFOX_PATH = os.path.join(DRIVER_DIR, 'geckodriver.exe')     # 火狐驱动文件路径
OPERA_PATH = os.path.join(DRIVER_DIR, 'operadriver.exe')     # 欧鹏驱动文件路径


def get_driver(browser=None):
    if browser == 'ie':
        driver = webdriver.Edge(EDGE_PATH)
    elif browser == 'firefox':
        driver = webdriver.Firefox(FIRFOX_PATH)
    elif browser == 'opera':
        driver = webdriver.Opera(OPERA_PATH)
    else:
        driver = webdriver.Chrome(CHROME_PATH)
    return driver


class Basic():
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def get_url(self, url, time=15):
        """最大化打开网页"""
        self.driver.implicitly_wait(time)
        self.driver.maximize_window()
        self.driver.get(url)

    def element(self, elementType, value, timeout=10):
        """定位元素"""
        try:
            if elementType == 'xpath':
                element = WebDriverWait(
                    self.driver, timeout, 1).until(
                    EC.presence_of_element_located(
                        (By.XPATH, value)))
                return element
            elif elementType == 'id':
                element = WebDriverWait(
                    self.driver, timeout, 1).until(
                    EC.presence_of_element_located(
                        (By.ID, value)))
                return element
            elif elementType == 'name':
                element = WebDriverWait(
                    self.driver, timeout, 1).until(
                    EC.presence_of_element_located(
                        (By.NAME, value)))
                return element
            elif elementType == 'class':
                element = WebDriverWait(
                    self.driver, timeout, 1).until(
                    EC.presence_of_element_located(
                        (By.CLASS_NAME, value)))
                return element
            elif elementType == 'link':
                element = WebDriverWait(
                    self.driver, timeout, 1).until(
                    EC.presence_of_element_located(
                        (By.LINK_TEXT, value)))
                return element
            elif elementType == 'css':
                element = WebDriverWait(
                    self.driver, timeout, 1).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, value)))
                return element
        except BaseException:
            self.logger.error("%s 页面未找到元素 %s" % (self, value))

    def elements(self, elementType, value, timeout=10):
        """定位一组元素"""
        try:
            if elementType == 'xpath':
                elements = WebDriverWait(
                    self.driver, timeout, 1).until(
                    EC.presence_of_all_elements_located(
                        (By.XPATH, value)))
                return elements
            elif elementType == 'id':
                elements = WebDriverWait(
                    self.driver, timeout, 1).until(
                    EC.presence_of_all_elements_located(
                        (By.ID, value)))
                return elements
            elif elementType == 'name':
                elements = WebDriverWait(
                    self.driver, timeout, 1).until(
                    EC.presence_of_all_elements_located(
                        (By.NAME, value)))
                return elements
            elif elementType == 'class':
                elements = WebDriverWait(
                    self.driver, timeout, 1).until(
                    EC.presence_of_all_elements_located(
                        (By.CLASS_NAME, value)))
                return elements
            elif elementType == 'link':
                elements = WebDriverWait(
                    self.driver, timeout, 1).until(
                    EC.presence_of_all_elements_located(
                        (By.LINK_TEXT, value)))
                return elements
            elif elementType == 'css':
                elements = WebDriverWait(
                    self.driver, timeout, 1).until(
                    EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, value)))
                return elements
        except BaseException:
            self.logger.error("%s 页面未找到元素 %s" % (self, value))

    def select_by_index(self, elementType, value, index):
        """通过所有index，0开始,定位元素"""
        try:
            element = self.element(elementType, value, timeout=10)
            Select(element).select_by_index(index)
        except BaseException:
            self.logger.error("%s 页面未找到元素 %s" % (self, value))

    def select_by_value(self, elementType, value, value1):
        """通过value定位元素"""
        try:
            element = self.element(elementType, value, timeout=10)
            Select(element).select_by_value(value1)
        except BaseException:
            self.logger.error("%s 页面未找到元素 %s" % (self, value))

    def select_by_text(self, elementType, value, text):
        """通过text定位元素"""
        try:
            element = self.element(elementType, value, timeout=10)
            Select(element).select_by_visible_text(text)
        except BaseException:
            self.logger.error("%s 页面未找到元素 %s" % (self, value))

    def text_perform(self, value1, value2):
        element1 = self.driver.find_element_by_css_selector(
            value1).find_element_by_css_selector(value2)
        return element1.text

    def clear(self, elementType, value):
        """清除文本框"""
        element = self.element(elementType, value)
        element.clear()

    def text(self, elementType, value):
        """获取文本内容"""
        element = self.element(elementType, value)
        return element.text

    def get_attribute(self, elementType, value, name):
        """获得属性"""
        element = self.element(elementType, value)
        return element.get_attribute(name)

    def location(self, elementType, value):
        """获得元素坐标"""
        element = self.element(elementType, value)
        return element.location

    def size(self, elementType, value):
        """获取元素尺寸"""
        element = self.element(elementType, value)
        return element.size

    def save_screenshot(self, filename):
        """截图"""
        self.driver.save_screenshot(filename)

    def current_url(self):
        """获取当前URL"""
        return self.driver.current_url

    def cookies(self):
        """获取当前COOKIES"""
        return self.driver.get_cookies()

    def title(self):
        """获取当前title"""
        return self.driver.title

    def quit(self):
        """关闭浏览器"""
        return self.driver.quit()

    def close(self):
        """关闭窗口"""
        return self.driver.close()

    def forward(self):
        """前进"""
        return self.driver.forward()

    def back(self):
        """后退"""
        return self.driver.back()

    def refresh(self):
        """刷新"""
        return self.driver.refresh()

    def click(self, elementType, value):
        """单击"""
        element = self.element(elementType, value)
        element.click()

    def click_perform(self, value1, value2):
        element1 = self.driver.find_element_by_css_selector(
            value1).find_element_by_css_selector(value2)
        element1.click()

    def move_to(self, elementType, value):
        """鼠标悬疑"""
        element = self.element(elementType, value)
        ActionChains(self.driver).move_to_element(element).perform()

    def context_click(self, elementType, value):
        """鼠标右键"""
        element = self.element(elementType, value)
        ActionChains(self.driver).context_click(element).perform()

    def drag_and_drop(self, elementType, value1, value2):
        """拖拽"""
        element = self.element(elementType, value1)
        target = self.element(elementType, value2)
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    def input(self, elementType, value, text):
        """清除输入框内容并发送文本"""
        element = self.element(elementType, value)
        # element.clear()
        element.send_keys(text)

    def input_perform(self, value1, value2, inputvalue):
        element1 = self.driver.find_element_by_css_selector(
            value1).find_element_by_css_selector(value2)
        element1.input(inputvalue)

    def space(self, elementType, value):
        element = self.element(elementType, value)
        element.send_keys(Keys.SPACE)

    def tab(self, elementType, value):
        element = self.element(elementType, value)
        element.send_keys(Keys.TAB)

    def esc(self, elementType, value):
        element = self.element(elementType, value)
        element.send_keys(Keys.ESCAPE)

    def enter(self, elementType, value):
        element = self.element(elementType, value)
        element.send_keys(Keys.ENTER)

    def ctrla(self, elementType, value):
        element = self.element(elementType, value)
        element.send_keys(Keys.CONTROL, 'a')

    def ctrlv(self, elementType, value):
        element = self.element(elementType, value)
        element.send_keys(Keys.CONTROL, 'v')

    def ctrlc(self, elementType, value):
        element = self.element(elementType, value)
        element.send_keys(Keys.CONTROL, 'c')

    def ctrlx(self, elementType, value):
        element = self.element(elementType, value)
        element.send_keys(Keys.CONTROL, 'x')

    def jump_off(self):
        """页面跳转后关闭窗口"""
        old_handle = self.driver.current_window_handle
        handles = self.driver.window_handles
        for handle in handles:
            if handle != old_handle:
                self.driver.switch_to.window(handle)
            else:
                self.driver.close()

    def jump(self):
        """页面跳转"""
        old_handle = self.driver.current_window_handle
        handles = self.driver.window_handles
        for handle in handles:
            if handle != old_handle:
                self.driver.switch_to.window(handle)

    def iframe(self, elementType, value):
        iframe = self.element(elementType, value)
        self.driver.switch_to.frame(iframe)

    def frame_back(self):
        self.driver.switch_to.default_content()

    def alert(self):
        self.driver.switch_to.alert.accept()

    def js_script(self, js):
        """运行JS脚本"""
        self.driver.execute_script(js)

    def js_fours_element(self, locator):
        """聚焦元素"""
        element = self.element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def js_scroll_top(self):
        """滑动到页面顶部"""
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        """滑动到页面底部"""
        js = "window.scrollTo(0, document.body.scrollHeight)"
        self.driver.execute_script(js)
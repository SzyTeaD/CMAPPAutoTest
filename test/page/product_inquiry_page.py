import time

from project.cmapp_test.config.config import NOW, SCREENSHOT_PATH, Config, DAY
from project.cmapp_test.test.page.login_page import Login
from utils.basic import browser, Basic


class ProductInquiry():
    def page(self,driver):
        # 商品询价
        driver.click('class', 'popup-item')
        time.sleep(1)
        driver.input('id', 'editor', NOW + '自动化商品询价单测试自动化商品询价单测试')
        driver.click('css', '[class="filter_confirm_btn filter_btn"]')
        driver.input('id', 'price', 40000)
        driver.clear('id', 'contact-num')
        driver.input('id', 'contact-num', 15132004444)
        driver.input('id', 'createTime1', DAY)
        try:
            time.sleep(1)
            driver.click('id', 'confirm-btn')
        except Exception:
            driver.save_screenshot(SCREENSHOT_PATH)
            print('询价失败')
        time.sleep(30)
        driver.click('css', '[class="btn btn-primary sureBtn"]')

if __name__ == '__main__':
    driver = browser()
    dr = Basic(driver)
    url = Config().get('PRODUCT_INQUIRY')
    dr.get_url(url)
    dr.click('class','inquiry-order')
    dr.jump_off()
    username = '600022_system'
    password = 'yw123456'
    Login().login(dr,username,password)
    time.sleep(2)
    dr.back()
    print(1)
    dr.refresh()
    dr.click('class','inquiry-order')
    ProductInquiry().page(dr)
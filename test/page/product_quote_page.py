import time

from project.cmapp_test.config.config import NOW, SCREENSHOT_PATH, Config, DAY
from project.cmapp_test.test.page.login_page import Login
from utils.basic import browser, Basic


class ProductQuote():
    def page(self, driver, price=40000):
        # 商品报价单
        time.sleep(1)
        driver.click('css', '[class="btn btn-primary btn-outline"]')
        time.sleep(1)
        driver.input('id', 'modal-price', price)
        driver.click(
            'css', '[class="btn btn-primary list-quote-confirm"]')
        driver.input('id', 'explainTextarea', NOW)
        driver.input('id', 'endtime', DAY)
        driver.input('id', 'deliTime', DAY)
        driver.clear('id', 'user_mobile')
        driver.input('id', 'user_mobile', 15542286637)
        driver.clear('id', 'user_email')
        driver.input('id', 'user_email', 'xiaotong.wang@zzj.com.cn')
        try:
            driver.click('id', 'btnConfirm')
            driver.click('css', '[class="btn btn-primary sureBtn"]')
            time.sleep(60)
            ii = driver.text('class', 'ht-modal-default-text')
            assert ii == '报价成功！'
            driver.click('css', '[class="btn btn-primary sureBtn"]')
        except Exception:
            driver.save_screenshot(SCREENSHOT_PATH)
            print('报价失败')


if __name__ == '__main__':
    driver = browser()
    dr = Basic(driver)
    url = Config().get('PRODUCT_QUOTE_URL')
    dr.get_url(url)
    username = '600606_system'
    password = 'yw123456'
    Login().login(dr, username, password)
    dr.click('css', '#quoteHandler > li:nth-child(2) > a > span.left')
    dr.jump_off()
    ProductQuote().page(dr)

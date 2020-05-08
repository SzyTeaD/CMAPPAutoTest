import time

from project.cmapp_test.config.config import SCREENSHOT_PATH, Config
from project.cmapp_test.test.page.login_page import Login
from project.cmapp_test.test.suite.button import Button
from utils.basic import browser, Basic


class ProductBuy():
    def page(self,driver):
        # 商品购买
        driver.click('id', 'popupAddress')
        time.sleep(1)
        driver.clear('name', 'num')
        driver.input('name', 'num', 15004598741)
        driver.clear('name', 'address')
        driver.input('name', 'address', '底密尔')
        driver.click(
            'css', '#popup-address > div.filter-attribute > div.filter_confirm > a')

        try:
            driver.click('id', 'confirm-btn')
            time.sleep(40)
            i = driver.text('class','ht-modal-default-text')
            assert i == '提交成功'
            driver.click('css', '[class ="btn btn-primary sureBtn"]')
        except Exception:
            driver.save_screenshot(SCREENSHOT_PATH)
            print('购买失败')

if __name__ == '__main__':
    driver = browser()
    dr = Basic(driver)
    btn = Button(dr)
    url = Config().get('PRODUCT_BUY')
    dr.get_url(url)
    buyerusr = Config().get('BUSR')
    buyerpsw = Config().get('BPSW')
    btn.buy()
    Login().login(dr, buyerusr, buyerpsw)
    btn.buy()
    try:
        dr.click('id', 'save')
    except Exception:
        pass
    ProductBuy().page(dr)

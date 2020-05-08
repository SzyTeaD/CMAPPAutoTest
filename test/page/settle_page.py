import time

from project.cmapp_test.config.config import Config, SCREENSHOT_PATH
from project.cmapp_test.test.page.login_page import Login
from utils.basic import browser, Basic


class Settle():
    def page(self, driver, num='1'):
        # 结算单
        if num == '1':
            driver.click('css',
                         '[class="ht-table-btn order-detail"]')
            driver.jump_off()
            try:
                driver.input('id', 'flowCode', '128306')
            except Exception:
                pass
            driver.clear('id', 'paymentBankAccount')
            driver.input('id', 'paymentBankAccount', '422060100100135825')
            driver.clear('id', 'receiveBankAccount')
            driver.input('id', 'receiveBankAccount', '422060100100135825')
            driver.click('id', 'btnSelectBank')
            time.sleep(1)
            driver.click(
                'css',
                '#bankListTable > table > tbody > tr > td:nth-child(1) > label > span')
            driver.click('id', 'btnChooseBankConfirm')
            time.sleep(1)
            driver.click(
                'css',
                '#paymentForm > div > div:nth-child(3) > div > div.ibox-content > div > div > ul > li:nth-child(9) > div > div.col-md-5 > div')
            time.sleep(1)
            driver.click('css', '[title="中国银行"]')
            try:
                driver.click('id', 'confirm')
                driver.click('css', '[class="btn btn-primary sureBtn"]')
                i = driver.text('class', 'ht-modal-default-text')
                assert i == '支付成功！'
                driver.click('css', '[class="btn btn-primary sureBtn"]')
            except Exception:
                print('支付失败')
            time.sleep(1)
        else:
            for i in range(int(num)):
                driver.click(
                    'css',
                    'body > div.container-cloud > div.container-main.clearfix.open-sidebar > div.main-content > div:nth-child(6) > div > div > div.ibox-content > div.row > div > div.table-list > div > div:nth-child(1) > ul.content-detail.row > li.col-md-1.content-operate')
                driver.jump_off()
                try:
                    driver.input('id', 'flowCode', '128306')
                except Exception:
                    pass
                driver.clear('id', 'paymentBankAccount')
                driver.input(
                    'id', 'paymentBankAccount', '422060100100135825')
                driver.clear('id', 'receiveBankAccount')
                driver.input(
                    'id', 'receiveBankAccount', '422060100100135825')
                driver.click('id', 'btnSelectBank')
                time.sleep(1)
                driver.click(
                    'css', '#bankListTable > table > tbody > tr > td:nth-child(1) > label > span')
                driver.click('id', 'btnChooseBankConfirm')
                time.sleep(1)
                driver.click(
                    'css',
                    '#paymentForm > div > div:nth-child(3) > div > div.ibox-content > div > div > ul > li:nth-child(9) > div > div.col-md-5 > div')
                time.sleep(1)
                driver.click('css', '[title="中国银行"]')
                try:
                    driver.click('id', 'confirm')
                    driver.click('css', '[class="btn btn-primary sureBtn"]')
                    i = driver.text('class', 'ht-modal-default-text')
                    assert i == '支付成功！'
                    driver.click('css', '[class="btn btn-primary sureBtn"]')
                except Exception:
                    driver.save_screenshot(SCREENSHOT_PATH)
                    print('支付失败')
                time.sleep(1)


if __name__ == '__main__':
    driver = browser()
    dr = Basic(driver)
    url = Config().get('SETTLE_URL')
    dr.get_url(url)
    username = '600022_system'
    password = 'yw123456'
    Login().login(dr, username, password)
    Settle().page(dr)

import time

from project.cmapp_test.config.config import SCREENSHOT_PATH, Config
from project.cmapp_test.test.page.login_page import Login
from utils.basic import browser, Basic


class Payfor():
    def page(self, driver, pact_num ,num='1'):
        # 支付单审批，num需要根据合同的节点数填写
        if num == '1':
            driver.click(
                'css', '[class="btn btn-primary btn-outline btn-sm"]')
            driver.click('id', 'btnSelectContract')
            time.sleep(1)
            driver.input('name', 'Q_contCode_SL', pact_num)
            driver.click('id', 'btnSearch')
            time.sleep(1)
            driver.click('class', 'form-control-radio')
            driver.click('id', 'btnSelect')
            time.sleep(1)
            driver.click(
                'css',
                '#payPlanShow > tbody > tr:nth-child(1) > td:nth-child(1) > label')
            driver.clear('name', 'remitAccountName')
            driver.input('name', 'remitAccountName', '底密尔')
            driver.clear('name', 'remitBackNum')
            driver.input('name', 'remitBackNum', '422060100100135825')
            try:
                driver.click('id', 'finalSubmit')
                i = driver.text('class', 'ht-modal-default-text')
                assert i == '添加成功！'
                driver.click('css', '[class="btn btn-primary sureBtn"]')
                print('添加付款成功')
            except Exception:
                print('添加付款失败')
            try:
                driver.click('class', 'btnFinish')
                driver.click('css', '[class="btn btn-primary sureBtn"]')
                i = driver.text('class', 'ht-modal-default-text')
                assert i == '合同付款流程通过！'
                driver.click('css', '[class="btn btn-primary sureBtn"]')
                print('合同付款流程通过')
            except Exception:
                print('合同付款流程失败')

        else:
            for i in range(int(num)):
                driver.click(
                    'css', '[class="btn btn-primary btn-outline btn-sm"]')
                driver.click('id', 'btnSelectContract')
                time.sleep(1)
                driver.input('name', 'Q_contCode_SL', pact_num)
                driver.click('id', 'btnSearch')
                time.sleep(1)
                driver.click('class', 'form-control-radio')
                driver.click('id', 'btnSelect')
                time.sleep(1)
                driver.click('css', '#payPlanShow > tbody > tr:nth-child(' +
                             str(int(i) + 1) + ') > td:nth-child(1) > label')
                driver.clear('name', 'remitAccountName')
                driver.input('name', 'remitAccountName', '底密尔')
                driver.clear('name', 'remitBackNum')
                driver.input('name', 'remitBackNum', '422060100100135825')
                try:
                    driver.click('id', 'finalSubmit')
                    i = driver.text('class', 'ht-modal-default-text')
                    assert i == '添加成功！'
                    driver.click('css', '[class="btn btn-primary sureBtn"]')
                    print('添加付款成功')
                except Exception:
                    print('添加付款失败')
                try:
                    driver.click('class', 'btnFinish')
                    driver.click('css', '[class="btn btn-primary sureBtn"]')
                    i = driver.text('class', 'ht-modal-default-text')
                    assert i == '合同付款流程通过！'
                    driver.click('css', '[class="btn btn-primary sureBtn"]')
                    print('合同付款流程通过')
                except Exception:
                    driver.save_screenshot(SCREENSHOT_PATH)
                    print('合同付款流程失败')


if __name__ == '__main__':
    driver = browser()
    dr = Basic(driver)
    url = Config().get('PAYFOR_URL')
    dr.get_url(url)
    username = '600022_system'
    password = 'yw123456'
    Login().login(dr, username, password)
    Payfor().page(dr)

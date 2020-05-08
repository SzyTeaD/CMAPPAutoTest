import time

from project.cmapp_test.config.config import NOW, SCREENSHOT_PATH, Config, DAY
from project.cmapp_test.test.page.login_page import Login
from utils.basic import browser, Basic


class Pact():
    def page(self, driver, inqnum, price, pact_name, num=1):
        # 生成合同
        # num 是合同节点数
        driver.click('id', 'btn-select-source')
        time.sleep(1)
        driver.input('id', 'inqId', inqnum)
        driver.click('css', '[class="btn btn-sm btn-primary btn-outline btn-search"]')
        driver.click('class','form-control-checkbox')
        driver.click(
            'css', '[class="btn btn-primary btn-select"]')
        driver.input('id', 'startTime', DAY)
        driver.input('id', 'endTime', DAY)
        driver.click('id', 'add-node')
        if num == 1:
            driver.input('id', 'time-node0', DAY)
            driver.click('id', 'time-node0')
            driver.input(
                'xpath',
                '//*[@id="table-time"]/tbody/tr/td[3]/div/input',
                '付款')
            driver.input(
                'xpath',
                '//*[@id="table-time"]/tbody/tr/td[4]/div/input',
                price)
        if num != 1:
            driver.input('id', 'time-node0', DAY)
            driver.click('id', 'time-node0')
            driver.input(
                'xpath',
                '//*[@id="table-time"]/tbody/tr/td[3]/div/input',
                '付款1')
            driver.input('xpath',
                         '//*[@id="table-time"]/tbody/tr/td[4]/div/input',
                         str(float(price) - float(num) + 1))
            for i in range(int(num) - 1):
                driver.click('id', 'add-node')
                driver.input('id', 'time-node' +
                             str((int(i) + 1)), DAY)
                driver.click('id', 'time-node' + str((int(i) + 1)))
                driver.input('xpath', '//*[@id="table-time"]/tbody/tr[' + str(
                    (int(i) + 2)) + ']/td[3]/div/input', '付款' + str((int(i) + 2)))
                driver.input(
                    'xpath', '//*[@id="table-time"]/tbody/tr[' + str((int(i) + 2)) + ']/td[4]/div/input', '1')
        driver.input('name', 'cont_name', NOW + pact_name)
        driver.input('name', 'target_name', DAY)
        driver.input('name', 'singDate', DAY)
        driver.input('name', 'Intr_code', DAY)
        try:
            driver.click('id', 'submit-final')
            i = driver.text('class', 'ht-modal-default-text')
            assert i == '请确认合同信息是否填写正确！'
            driver.click('css', '[class="btn btn-primary sureBtn"]')
            print('合同成功')
        except Exception:
            driver.save_screenshot(SCREENSHOT_PATH)
            print('合同失败')


if __name__ == '__main__':
    driver = browser()
    dr = Basic(driver)
    url = Config().get('PACT_URL')
    dr.get_url(url)
    username = '600022_system'
    password = 'yw123456'
    Login().login(dr, username, password)
    Pact().page(dr, 476, '合同')

import random
import time

from config.pathes import NOW, SCREENSHOT_PATH
from utils.BasicPage import browser, Basic


class CapacityInquiry():
    def page(self,driver):
        # 能力询价·
        driver.input('name', 'amount', 1)
        driver.input('name', 'expectOffer', 9999)
        driver.input(
            'id',
            'editor',
            NOW +
            '流程自动化测试流程自动化测试流程自动化测试流程自动化测试')
        driver.input('name', 'contact', '流程自动化测试' +
                          str(random.randint(0, 10)))
        driver.input('name', 'mobile', 15004598741)
        driver.input('name', 'email', '15004598741@163.com')
        try:
            driver.click('id', 'btnSubmit')
            driver.click('css', '[class="btn btn-primary sureBtn"]')
            time.sleep(1)
            i = driver.text('css','[class="modal-body text-center"]')
            assert i == '操作成功，请耐心等待对方企业回应'
            driver.click('id', 'toCMCapability')
            print('询价单成功')

        except Exception :
            driver.save_screenshot(SCREENSHOT_PATH)
            print('询价单失败')

if __name__ == '__main__':
    driver = browser()
    dr = Basic(driver)
    url = Config().get('CAPACITY_INQUIRY_URL')
    dr.get_url(url)
    dr.click('class','inquiry')
    dr.jump_off()
    username = '600022_system'
    password = 'yw123456'
    Login().login(dr,username,password)
    CapacityInquiry().page(dr)
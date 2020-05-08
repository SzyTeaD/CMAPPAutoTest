from project.cmapp_test.config.config import NOW, SCREENSHOT_PATH, Config, DAY
from project.cmapp_test.test.page.login_page import Login
from utils.basic import browser, Basic



class CapacityQuote():
    def page(self, driver,yuzhi):
        # 能力报价单
        driver.click('css', '[class="btn btn-primary btn-outline"]')
        driver.input('id', 'modal-price', 40000)
        driver.input('id', 'tcjIpt', 99)
        driver.clear('id', 'dfyzIpt')
        driver.input('id', 'dfyzIpt', yuzhi)
        driver.click(
            'css', '[class="btn btn-primary list-quote-confirm"]')
        driver.input('id', 'explainTextarea', NOW)
        driver.clear('id', 'user_mobile')
        driver.input('id', 'user_mobile', 15542286637)
        driver.clear('id', 'user_email')
        driver.input('id', 'user_email', 'xiaotong.wang@zzj.com.cn')
        driver.input('id', 'endtime', DAY)
        try:
            driver.click('id', 'btnConfirm')
            driver.click('css', '[class="btn btn-primary sureBtn"]')
            ii = driver.text('class','ht-modal-default-text')
            assert ii == '报价成功！'
            driver.click('css', '[class="btn btn-primary sureBtn"]')
        except Exception:
            driver.save_screenshot(SCREENSHOT_PATH)
            print('报价失败')


if __name__ == '__main__':
    driver = browser()
    dr = Basic(driver)
    url = Config().get('CAPACITY_QUOTE_URL')
    dr.get_url(url)
    username = '600606_system'
    password = 'yw123456'
    Login().login(dr,username,password)
    dr.click('css','#block3 > div.ibox-content.ibox-height312 > ul.list-box.list-box-first > li:nth-child(2) > a > span.left')
    dr.jump_off()
    CapacityQuote().page(dr,100)
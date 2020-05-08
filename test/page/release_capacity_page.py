import os
import random
import time

from project.cmapp_test.config.config import DATA_PATH, NOW, Config
from project.cmapp_test.test.page.login_page import Login
from project.cmapp_test.test.suite.button import Button
from utils.basic import browser, Basic
from utils.file_reader import ExcelReader
from utils.generator import random_str


class CapacityRelease():

    def Type(self, i):
        f = os.path.join(DATA_PATH, 'relese.xlsx')
        reader = ExcelReader(f, title_line=True)
        type = reader.data[i]
        return type

    def page(self,driver):
        # 发布能力
        driver.click(
            'xpath',
            '//*[@id="isJoinCloud"]/div[1]/label')
        driver.click('class', 'cascade-text')
        driver.click('css', self.Type(random.randint(1,7))['data-level-1'])
        driver.click('css', self.Type(random.randint(1,7))['data-level-2'])
        # driver.click('css', '[data-id="10302"]')
        driver.click('css', '[class="cascade-confirm"]')
        driver.input('name', 'capandproname', '能力' + NOW + random_str(1,2))
        driver.input('name', 'chargeunit', '台')
        driver.input('name', 'price', random.randint(100,1000000))
        driver.input('name','certificate_id1',self.Type(random.randint(1,7))['certificate_id1'])
        time.sleep(1)
        driver.click('id', 'clipBtn')
        driver.input('id','editor',random_str(22,88))
        driver.clear('name','address')
        driver.input('name','address','北京')
        driver.click('id','editor')
        driver.click('id', 'inq-publish')
        Button(driver).surebtn()



if __name__ == '__main__':
    driver = browser()
    dr = Basic(driver)
    url = Config().get('CAPACITY_RELEASE_URL')
    dr.get_url(url)
    username = '600633_system'
    password = 'yw123456'
    Login().login(dr,username,password)
    CapacityRelease().page(dr)
    for i in range(20):
        dr.click('id','addBtn')
        dr.jump_off()
        CapacityRelease().page(dr)

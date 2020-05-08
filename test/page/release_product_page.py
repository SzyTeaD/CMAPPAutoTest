import os
import random
import time

from project.cmapp_test.config.config import DATA_PATH, NOW, Config
from project.cmapp_test.test.page.login_page import Login
from project.cmapp_test.test.suite.button import Button
from utils.basic import browser, Basic
from utils.file_reader import ExcelReader
from utils.generator import random_str, random_phone_number


class ProductRelease():

    def Type(self,i):
        f = os.path.join(DATA_PATH, 'relese.xlsx')
        reader = ExcelReader(f , title_line=True)
        type = reader.data[i]
        return type

    def page(self,driver):
        '''发布商品'''
        driver.click('class','form-control-radio')
        driver.click('class','cascade-text')
        driver.click('css', self.Type(random.randint(1,7))['data-level-1'])
        driver.click('css', self.Type(random.randint(1,7))['data-level-2'])
        driver.click('class','cascade-confirm')
        driver.input('css','#form1 > div:nth-child(1) > div > div.ibox-content.clearfix > div > div:nth-child(4) > div.col-md-5 > input','商品'+NOW + random_str(2,5))
        driver.input('name', 'material_desc',random_str(20,88))
        driver.input('name','certificate_id1',self.Type(random.randint(1,7))['certificate_id1'])
        driver.click('id', 'clipBtn')
        driver.input('name', 'unit', '个')
        driver.input('name', 'stock', random.randint(22,99))
        driver.input('name', 'supply_cycle', random.randint(1,99))
        driver.input('name', 'manufacture', random_str(2,5))
        driver.input('xpath', '//*[@id="ht-edit-table"]/tbody/tr/td[4]/div/input', 199)
        driver.input('name', 'priceSingle', random.randint(10, 99))
        driver.input('name', 'discountSingle', random.randint(1,10))
        driver.input('name', 'royaltyRate', random.randint(1,50))
        driver.clear('name', 'contacts')
        driver.input('name', 'contacts', random_str(5,10))
        driver.clear('name', 'contacts_phone')
        driver.input('name', 'contacts_phone', random_phone_number())
        driver.click('id', 'confirm')


if __name__ == '__main__':
    driver = browser()
    dr = Basic(driver)
    url = Config().get('CAPACITY_RELEASE_URL')
    dr.get_url(url)
    username = '600606_system'
    password = 'yw123456'
    Login().login(dr,username,password)
    ProductRelease().page(dr)
    for i in range(20):
        dr.click('id','addBtn')
        dr.jump_off()
        ProductRelease().page(dr)


import os
import time
import unittest

from project.cmapp_test.config.config import DATA_PATH, Config
from project.cmapp_test.test.page.capacity_inquiry_page import CapacityInquiry
from project.cmapp_test.test.page.capacity_quote_page import CapacityQuote
from project.cmapp_test.test.page.login_page import Login
from project.cmapp_test.test.page.logout_page import Logout
from project.cmapp_test.test.page.pact_page import Pact
from project.cmapp_test.test.page.payfor_page import Payfor
from project.cmapp_test.test.page.settle_page import Settle
from project.cmapp_test.test.suite.button import Button
from project.cmapp_test.test.suite.flow import Flow
from utils.basic import Basic, browser
from utils.file_reader import ExcelReader, folwType


class persen_marketing_share_product(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = browser()
        self.dr = Basic(self.driver)
        self.btn = Button(self.dr)
        self.flow = Flow(self.dr)
        self.tp = folwType(os.path.join(DATA_PATH, 'yx_flow.xlsx'), sheet=2)
        self.pact_num = None

    def test1_share_product(self):
        method = int(self.tp['method'])
        marketusr = Config().get('MKTUSR')
        marketpsw = Config().get('MKTPSW')
        url = Config().get('HOME_URL')
        self.dr.get_url(url)
        Login().login(self.dr, marketusr, marketpsw)
        time.sleep(1)
        if method == 1:
            self.flow.team_share_capacity_flow('航天云网')
        else:
            self.flow.share_capacity_flow('航天云网')
            globals()['product_url'] = self.dr.get_attribute(
                'id', 'firstProduct', 'value')

    def test2_capacity_inquiry(self):
        time.sleep(1)
        Logout().logout(self.dr)
        globals()['capacity_url'] = capacity_url.replace('www', 'beta2019')
        self.dr.get_url(capacity_url)
        buyerusr = Config().get('BUSR')
        buyerpsw = Config().get('BPSW')
        self.btn.capacity_inquiry()
        self.dr.jump_off()
        Login().login(self.dr, buyerusr, buyerpsw)
        CapacityInquiry().page(self.dr)
        # 获取订单号
        globals()['inq_num'] = self.dr.text(
            'css',
            '#htCheck > div:nth-child(1) > ul.content-title.row > li.col-md-11 > span:nth-child(2) > span')
        # 获取询价主题
        globals()['inq_them'] = self.dr.text(
            'css',
            '#htCheck > div:nth-child(1) > ul.content-title.row > li.col-md-11 > span:nth-child(1)')

        # 判断是否有云端营销标签
        label = self.dr.text('css', '[class="label label-warning"]')
        self.assertEqual('云端营销', label, label)

    def test3_capacity_quote(self):
        time.sleep(1)
        Logout().logout(self.dr)
        url = Config().get('QUOTE_WX_URL')
        self.dr.get_url(url)
        sellerusr = Config().get('SUSR')
        sellerpsw = Config().get('SPSW')
        Login().login(self.dr, sellerusr, sellerpsw)
        self.dr.click('css', '[class="confirmCash btn btn-primary btn-outline"]')
        CapacityQuote().page(self.dr, 100)

    def test4_pact_page(self):
        time.sleep(1)
        Logout().logout(self.dr)
        url = Config().get('PACT_GWX_URL')
        self.dr.get_url(url)
        buyerusr = Config().get('BUSR')
        buyerpsw = Config().get('BPSW')
        Login().login(self.dr, buyerusr, buyerpsw)
        self.dr.click('link', '我要采购')
        self.dr.click('link', '所有外协需求')
        self.dr.jump_off()
        self.flow.youxuan_flow()
        self.flow.add_buy_capacity_pact_flow()
        Pact().page(self.dr, 40000, ' 能力询价')

    def test5_approve_sell_pact(self):
        time.sleep(1)
        Logout().logout(self.dr)
        url = Config().get('PACT_YWX_URL')
        self.dr.get_url(url)
        sellerusr = Config().get('SUSR')
        sellerpsw = Config().get('SPSW')
        Login().login(self.dr, sellerusr, sellerpsw)
        self.flow.sell_unapprove_flow()

    def test6_approve_buy_pact(self):
        time.sleep(1)
        Logout().logout(self.dr)
        url = Config().get('PACT_GWX_URL')
        self.dr.get_url(url)
        buyerusr = Config().get('BUSR')
        buyerpsw = Config().get('BPSW')
        Login().login(self.dr, buyerusr, buyerpsw)
        self.flow.buy_unapprove_unsign_flow()

    def test7_settle(self):
        self.dr.click('link', '结算管理')
        self.btn.enter_wx_payfor()
        Payfor().page(self.dr)
        self.btn.enter_wx_settle()
        Settle().page(self.dr)

    def test8_payment(self):
        time.sleep(1)
        Logout().logout(self.dr)
        url = Config().get('SETTLE_YWX_URL')
        self.dr.get_url(url)
        sellerusr = Config().get('SUSR')
        sellerpsw = Config().get('SPSW')
        Login().login(self.dr, sellerusr, sellerpsw)
        self.flow.sure_settle_flow()
        self.flow.payment_flow()

    @classmethod
    def tearDownClass(cls):
        print('营销员账号：158015900000')
        print('买家账号：600022_system')
        print('卖家账号：600633_system')


if __name__ == '__main__':
    unittest.main()

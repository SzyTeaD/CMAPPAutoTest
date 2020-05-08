import os
import time
import unittest

from project.cmapp_test.config.config import DATA_PATH, Config
from project.cmapp_test.test.page.login_page import Login
from project.cmapp_test.test.page.logout_page import Logout
from project.cmapp_test.test.page.pact_page import Pact
from project.cmapp_test.test.page.payfor_page import Payfor
from project.cmapp_test.test.page.product_buy_page import ProductBuy
from project.cmapp_test.test.page.settle_page import Settle
from project.cmapp_test.test.suite.button import Button
from project.cmapp_test.test.suite.flow import Flow
from utils.basic import Basic, browser
from utils.file_reader import folwType


class persen_marketing_share_product(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = browser()
        self.dr = Basic(self.driver)
        self.btn = Button(self.dr)
        self.flow = Flow(self.dr)
        self.tp = folwType(os.path.join(DATA_PATH, 'yx_flow.xlsx'))
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
            self.flow.team_share_product_flow('航天云网')
        else:
            self.flow.share_product_flow('航天云网')
            globals()['product_url'] = self.dr.get_attribute(
                'id', 'firstProduct', 'value')

    def test2_product_buy(self):
        time.sleep(1)
        Logout().logout(self.dr)
        self.dr.get_url(product_url)
        buyerusr = Config().get('BUSR')
        buyerpsw = Config().get('BPSW')
        self.btn.buy()
        Login().login(self.dr, buyerusr, buyerpsw)
        self.btn.buy()
        try:
            self.dr.click('id', 'save')
        except Exception:
            pass
        globals()['product_price'] = self.dr.text('class', 'price')
        ProductBuy().page(self.dr)

    def test3_pact_page(self):
        self.dr.get_url(
            'http://test.etpss.casicloud.com/home/ywgzs/gyl/inquiry/WG/dataList.html')
        # 获取订单号
        inq_num = self.dr.text(
            'css',
            '#htCheck > div:nth-child(1) > ul.content-title.row > li.col-md-11 > span:nth-child(2) > span')
        # 判断是否有云端营销标签
        label = self.dr.text('css', '[class="label label-warning"]')
        self.assertEqual('云端营销', label, label)
        self.flow.add_buy_product_pact_flow()
        Pact().page(
            self.dr,
            inq_num,
            product_price,
            self.tp['pact_name'],
            self.tp['num'])
        globals()['pact_id'] = self.dr.get_attribute(
            'css', '[class="content-detail row cm"]', 'data-id')

    def test4_approve_sell_pact(self):
        time.sleep(1)
        Logout().logout(self.dr)
        url = Config().get('PACT_YWG_URL')
        self.dr.get_url(url)
        sellerusr = Config().get('SUSR')
        sellerpsw = Config().get('SPSW')
        Login().login(self.dr, sellerusr, sellerpsw)
        time.sleep(1)
        pact_ID = self.dr.get_attribute(
            'css', '[class="content-detail row cm"]', 'data-id')
        self.flow.sell_unapprove_flow()
        if pact_id != pact_ID:
            print('审批合同不是购买的签单合同，合同编号是：%s' % pact_ID)

    def test5_approve_buy_pact(self):
        time.sleep(1)
        Logout().logout(self.dr)
        url = Config().get('PACT_GWG_URL')
        self.dr.get_url(url)
        buyerusr = Config().get('BUSR')
        buyerpsw = Config().get('BPSW')
        Login().login(self.dr, buyerusr, buyerpsw)
        self.flow.buy_unapprove_unsign_flow()
        pact_ID = self.dr.get_attribute(
            'css', '[class="content-detail row cm"]', 'data-id')
        if pact_id != pact_ID:
            print('审批合同不是购买的签单合同，合同编号是：%s' % pact_ID)

    def test6_settle(self):
        self.pact_num = self.dr.text(
            'css',
            '#htTable > div > div:nth-child(1) > ul.content-title.row > li.col-md-11 > span:nth-child(2)')
        self.pact_num = self.pact_num.split('：')[1]
        globals()['pactNum'] = self.pact_num
        self.dr.refresh()
        self.dr.click('link', '结算管理')
        time.sleep(1)
        self.btn.enter_wg_payfor()
        Payfor().page(self.dr, self.pact_num, self.tp['num'])
        self.btn.enter_wg_settle()
        self.dr.input('name', 'Q_inquirytheme_SL', self.pact_num)
        self.dr.click('id', 'searchBtn')
        Settle().page(self.dr, self.tp['num'])

    def test7_payment(self):
        time.sleep(1)
        Logout().logout(self.dr)
        url = Config().get('SETTLE_YWG_URL')
        self.dr.get_url(url)
        sellerusr = Config().get('SUSR')
        sellerpsw = Config().get('SPSW')
        Login().login(self.dr, sellerusr, sellerpsw)
        self.flow.sure_settle_flow(pactNum, int(self.tp['num']))
        self.flow.payment_flow()
        self.dr.input('name', 'contractCode', pactNum)
        self.dr.click('id', 'filter')
        time.sleep(2)
        # pact_id = "\"" + self.pact_num + "\""
        self.dr.click('css', '[class="ht-table-btn confirmCash"]')
        self.btn.surebtn()
        i = self.dr.text('class', 'ht-modal-default-text')
        self.assertEqual('兑付成功', i, i)
        globals()['cash_num'] = self.dr.text(
            'css',
            '#htTable > div > div:nth-child(1) > ul.content-detail.row > li.col-md-2.content-other > div > span')
        self.btn.surebtn()

    def test8_cash(self):
        time.sleep(1)
        Logout().logout(self.dr)
        url = Config().get('CASH_URL')
        self.dr.get_url(url)
        sellerusr = Config().get('SUSR')
        sellerpsw = Config().get('SPSW')
        Login().login(self.dr, sellerusr, sellerpsw)
        self.dr.input('name', 'cash-code', cash_num)
        self.dr.click('id', 'filter')
        self.dr.click('class', 'confirmCash')
        self.btn.surebtn()
        i = self.dr.text('class', 'ht-modal-default-text')
        self.assertEqual('确认兑付成功', i, i)
        self.btn.surebtn()

    @classmethod
    def tearDownClass(self):
        self.dr.quit()
        print('营销员账号：158015900000')
        print('卖家账号：15801590000')
        print('买家账号：600022_system')


if __name__ == '__main__':
    unittest.main()

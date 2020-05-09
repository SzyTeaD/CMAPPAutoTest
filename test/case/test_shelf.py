import time
import unittest

from config.setting import TEST, TEST_SHELF_URL
from test.page.login_page import login
from test.page.shelfPage import ShelfPage
from utils.BasicPage import Basic, get_driver
from utils.generator import random_str
from utils.log import Logger

"""
testing_environmental = TEST登录测试环境，
testing_environmental = FORMAL登陆正式环境，
"""
testing_environmental = TEST
CASE_NAME = 'ShelfTest'


class Shelf(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.START_TIME = time.time()
        self.logger = Logger(CASE_NAME).get_logger()
        self.driver = get_driver()
        self.dr = Basic(self.driver, self.logger)
        self.p = ShelfPage(self.dr)

    def test1_login(self):
        """登陆账号"""
        MarketerName = testing_environmental.get('MarketerName')
        MarketerPassword = testing_environmental.get('MarketerPassword')
        shelf_url = TEST_SHELF_URL
        self.logger.info('测试用例：%s，开始执行!' % CASE_NAME)
        try:
            self.dr.get_url(shelf_url)
            login(self.dr, MarketerName, MarketerPassword)
            self.logger.info('登陆成功,营销员账号是：%s' % MarketerName)
        except:
            self.logger.error('登陆失败,营销员账号是：%s' % MarketerName)

    @unittest.skip('卡顿')
    def test2_operationShelf(self):
        """货架增删改查测试"""
        self.logger.info('执行货架增删改查测试：')
        newShelfName = random_str(4, 6)  # 新建货架名称
        _newShelfName = "\"" + newShelfName + "\""
        try:
            # 新建货架
            self.p.add_shelf()
            self.p.input_shelfName(newShelfName)
            self.p.primaryBtn()
            resAddInfo = self.p.shelf_txt()
            self.p.sureBtn()
            self.logger.info(resAddInfo)
            time.sleep(1)

            # 复制货架
            self.dr.click_perform(
                '[data-name=%s]' % _newShelfName,
                '[class="btnCopyShelf"]')
            self.p.sureBtn()
            resCopyeInfo = self.p.shelf_txt()
            self.logger.warning(resCopyeInfo)
            self.assertEqual('复制成功', resCopyeInfo, resCopyeInfo)
            self.p.sureBtn()
            time.sleep(1)

            # 编辑货架
            reName = random_str(4, 6)  # 修改后的货架名称
            _reName = "\"" + reName + "\""
            self.dr.click_perform(
                '[data-name=%s]' % newShelfName,
                '[class="btnModifyShelf"]')
            time.sleep(1)
            self.dr.clear('name', 'shelfname')
            self.dr.input('name', 'shelfname', reName)
            self.dr.click('id', 'modifyShelfName')
            resEditInfo = self.p.shelf_txt()
            self.logger.warning(resEditInfo)
            self.assertEqual('编辑成功', resEditInfo, resEditInfo)
            self.p.sureBtn()

            # 删除货架
            time.sleep(1)
            self.dr.click_perform(
                '[data-name=%s]' % _reName,
                '[class="btnDeleteShelf"]')
            self.p.sureBtn()
            resDelInfo = self.p.shelf_txt()
            self.p.sureBtn()
            self.logger.warning(resDelInfo)
            self.assertEqual('删除成功', resDelInfo, resDelInfo)
            # 删除复制的货架
            time.sleep(1)
            self.dr.click_perform(
                '[data-name=%s]' % _newShelfName,
                '[class="btnDeleteShelf"]')
            self.p.sureBtn()
            resDelInfo2 = self.p.shelf_txt()
            self.p.sureBtn()
            self.logger.warning(resDelInfo)
            self.assertEqual('删除成功', resDelInfo2, resDelInfo2)
            self.logger.info('货架增删改查测试执行通过！')
        except:
            self.logger.error('Operation Shelf Error')

    def test2_shareShelf(self):
        """分享货架"""
        time.sleep(1)
        self.dr.click_perform(
            '[class="table-list-title row hidden-xs"]',
            '[class="glyphicon glyphicon-ok"]')
        self.dr.click('id', 'btnShareShelves')
        time.sleep(1)
        self.dr.click('css', '[spm="cloudmarketing.shelflist.shareshelfcopy"]')
        self.p.sureBtn()
        path1 = self.dr.js_script("return jQuery('[id=copyPath]').val();")
        self.dr.click('class', 'close')
    #
    # @unittest.skip('卡顿')
    # def test8_product_management(self):
    #     time.sleep(1)
    #     self.dr.click_perform('[data-name="默认货架"]', '[target="_blank"]')
    #     self.dr.jump_off()
    #     time.sleep(1)
    #     # 找货
    #     self.dr.click('css', '[href="/home/cloudmarketing/hyzx"]')
    #     self.flow.product_selecet('沈阳')
    #     self.flow.join_shelf()
    #     self.dr.click_perform('[data-name="默认货架"]', '[target="_blank"]')
    #     self.dr.jump_off()
    #     # 下架
    #     self.dr.click('css', '[class="off-shelf off-goods"]')
    #     self.btn.surebtn()
    #     i = self.btn.shelf_txt()
    #     self.assertEqual('下架成功', i, i)
    #     self.btn.surebtn()
    #     self.dr.click('id', 'offShelf')
    #     # 上架
    #     self.dr.click('css', '[class="on-shelf on-goods"]')
    #     self.btn.surebtn()
    #     i = self.btn.shelf_txt()
    #     self.assertEqual('上架成功', i, i)
    #     self.btn.surebtn()
    #     # 删除
    #     self.dr.click('css', '[class="delete-shelf delete-goods"]')
    #     self.btn.surebtn()
    #     i = self.btn.shelf_txt()
    #     self.assertEqual('删除成功', i, i)
    #     self.btn.surebtn()
    #     # 批量管理
    #     self.dr.click('id', 'show-btn')
    #
    # @unittest.skip('卡顿')
    # def test9_capablity_management(self):
    #     # 找货
    #     self.dr.click('css', '[href="/home/cloudmarketing/hyzx"]')
    #     self.dr.input('id', 'newKeyword', '沈阳')
    #     self.dr.click('class', 'new_search_btn')
    #     time.sleep(1)
    #     self.dr.click('css', '#capacity > span')
    #     self.flow.join_shelf()
    #     self.dr.click_perform('[data-name="默认货架"]', '[target="_blank"]')
    #     self.dr.jump_off()
    #     # 点击能力标签
    #     self.dr.click('css', '[class="btn btn-white"]')
    #     # 下架
    #     self.dr.click('css', '[class="off-shelf off-capablity"]')
    #     self.btn.surebtn()
    #     i = self.btn.shelf_txt()
    #     self.assertEqual('下架成功', i, i)
    #     self.btn.surebtn()
    #     self.dr.click('id', 'offShelf')
    #     # 上架
    #     self.dr.click('css', '[class="on-shelf on-capablity"]')
    #     self.btn.surebtn()
    #     i = self.btn.shelf_txt()
    #     self.assertEqual('上架成功', i, i)
    #     self.dr.click('css', '[class="btn btn-primary sureBtn"]')
    #     # 删除
    #     self.dr.click('css', '[class="delete-shelf delete-capablity"]')
    #     self.btn.surebtn()
    #     i = self.btn.shelf_txt()
    #     self.assertEqual('删除成功', i, i)
    #     self.btn.surebtn()
    #     # 批量管理
    #     self.dr.click('id', 'show-btn')

    @classmethod
    def tearDownClass(self):

        # self.dr.quit()
        END_TIME = time.time()
        RUN_TIME = round((END_TIME - self.START_TIME), 2)
        self.logger.info('用例执行时长：%s秒' % RUN_TIME)


if __name__ == '__main__':
    unittest.main()

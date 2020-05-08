import time
import unittest

from config.pathes import PROJECTINFO
from config.setting import TEST, TEST_SHELF_URL
from test.page.login_page import login
from utils.BasicPage import browser, Basic
from utils.FileReader import YamlReader
from utils.generator import random_str
from utils.log import Logger


class Shelf(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = browser()
        self.dr = Basic(self.driver)
        self.logger = Logger('TestShelfCMAPP').get_logger()
        self.projectinfo = YamlReader(PROJECTINFO)

        self.name = random_str(4, 6)  # 新建货架名称
        self.name_inele = "\"" + self.name + "\""
        self.new_name = random_str(4, 6)  # 修改后的货架名称
        self.new_name_inele = "\"" + self.new_name + "\""

    def test1_login(self):
        """
        testing_environmental = TEST登录测试环境，
        testing_environmental = FORMAL登陆正式环境，
        """
        testing_environmental = TEST
        MarketerName = testing_environmental.get('MarketerName')
        MarketerPassword = testing_environmental.get('MarketerPassword')
        shelf_url = TEST_SHELF_URL
        self.logger.info('测试项目：%s')
        try:
            self.dr.get_url(shelf_url)
            login(self.dr, MarketerName, MarketerPassword)
            self.logger.info('登陆成功')
        except:
            self.logger.info('登陆失败')

    # def test2_addshelf(self):
    #     '''新建货架'''
    #     self.btn.add_shelf()
    #     self.btn.newshelfname(self.name)
    #     self.btn.primarybtn()
    #     time.sleep(1)
    #     shelf_name = self.dr.text('css', '[title=' + self.name_inele + ']')
    #     self.btn.surebtn()
    #     self.assertEqual(shelf_name, self.name, '创建货架失败')
    #
    # def test3_copyshelf(self):
    #     '''复制货架'''
    #     time.sleep(1)
    #     self.dr.click_perform(
    #         '[data-name=' + self.name_inele + ']',
    #         '[class="btnCopyShelf"]')
    #     self.btn.surebtn()
    #     self.btn.shelf_txt()
    #     i = self.btn.shelf_txt()
    #     self.assertEqual('复制成功', i, i)
    #     self.btn.surebtn()
    #
    # def test4_Modifyshelf(self):
    #     '''编辑货架'''
    #     time.sleep(1)
    #     self.dr.click_perform(
    #         '[data-name=' + self.name + ']',
    #         '[class="btnModifyShelf"]')
    #     time.sleep(1)
    #     self.dr.clear('name', 'shelfname')
    #     self.dr.click('id', 'modifyShelfName')
    #     i = self.btn.shelf_txt()
    #     self.btn.surebtn()
    #     self.assertEqual('请输入货架名称', i, i)
    #     self.dr.input('name', 'shelfname', self.new_name)
    #     self.dr.click('id', 'modifyShelfName')
    #     i = self.btn.shelf_txt()
    #     self.btn.surebtn()
    #     self.assertEqual('编辑成功', i, i)
    #
    # def test5_delshelf(self):
    #     '''删除货架'''
    #     time.sleep(1)
    #     self.dr.click_perform(
    #         '[data-name=' + self.name_inele + ']',
    #         '[class="btnDeleteShelf"]')
    #     self.btn.surebtn()
    #     i = self.btn.shelf_txt()
    #     self.btn.surebtn()
    #     self.assertEqual('删除成功', i, i)
    #
    # def test6_delshelf(self):
    #     '''删除复制的货架'''
    #     time.sleep(1)
    #     self.dr.click_perform(
    #         '[data-name=' + self.new_name_inele + ']',
    #         '[class="btnDeleteShelf"]')
    #     self.btn.surebtn()
    #     i = self.btn.shelf_txt()
    #     self.btn.surebtn()
    #     self.assertEqual('删除成功', i, i)
    #
    # def test7_shareallshelf(self):
    #     '''分享货架'''
    #     time.sleep(1)
    #     self.dr.click_perform(
    #         '[class="table-list-title row hidden-xs"]',
    #         '[class="glyphicon glyphicon-ok"]')
    #     self.dr.click('id', 'btnShareShelves')
    #     time.sleep(1)
    #     self.dr.click('css', '[spm="cloudmarketing.shelflist.shareshelfcopy"]')
    #     self.btn.surebtn()
    #     path1 = self.dr.js_script("return jQuery('[id=copyPath]').val();")
    #     self.dr.click('class', 'close')
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
        pass
        # self.dr.quit()


if __name__ == '__main__':
    unittest.main()

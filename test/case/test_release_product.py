import time
import unittest

from project.cmapp_test.config.config import Config
from project.cmapp_test.test.page.login_page import Login
from project.cmapp_test.test.page.release_product_page import ProductRelease
from project.cmapp_test.test.suite.button import Button
from project.cmapp_test.test.suite.flow import Flow
from utils.basic import browser, Basic


class ReleaseCapacity(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = browser()
        self.dr = Basic(self.driver)
        self.btn = Button(self.dr)
        self.flow = Flow(self.dr)

    def test1_login(self):
        sellerusr = Config().get('SUSR')
        sellerpsw = Config().get('SPSW')
        url = Config().get('PRODUCT_RELEASE_URL')
        self.dr.get_url(url)
        Login().login(self.dr, sellerusr, sellerpsw)

    def test2_release(self):
        try:
            self.dr.click('css', '[spm="cb.yxzx.spfb"]')
            Button(self.dr).surebtn()
        except Exception:
            pass
        ProductRelease().page(self.dr)

    @unittest.skip('跳过')
    def test3_release(self):
        for i in range(20):
            self.dr.refresh()
            Button(self.dr).surebtn()
            # self.dr.click('id', 'addBtn')
            # self.dr.jump_off()
            time.sleep(1)
            self.dr.js_scroll_top()
            ProductRelease().page(self.dr)


if __name__ == '__main__':
    unittest.main()

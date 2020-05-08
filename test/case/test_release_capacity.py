import unittest

from project.cmapp_test.config.config import Config
from project.cmapp_test.test.page.login_page import Login
from project.cmapp_test.test.page.release_capacity_page import CapacityRelease
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
        url = Config().get('CAPACITY_RELEASE_URL')
        self.dr.get_url(url)
        Login().login(self.dr, sellerusr, sellerpsw)

    def test2_release(self):
        CapacityRelease().page(self.dr)

    @unittest.skip('跳过')
    def test3_release(self):
        for i in range(2):
            self.dr.click('id', 'addBtn')
            self.dr.jump_off()
            CapacityRelease().page(self.dr)

if __name__ == '__main__':
    unittest.main()

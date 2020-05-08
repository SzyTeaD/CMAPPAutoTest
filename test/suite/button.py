class Button():
    def __init__(self, driver):
        self.driver = driver

    def enter_center(self):
        '''点击营销中心'''
        self.driver.click('css', '[data-sidebar="bs-yxzx"]')

    def enter_sell_pact(self):
        self.driver.click('link', '销售合同')

    def enter_gyl(self):
        # 点击供应链
        self.driver.click('css', '[class="icon-s icon-arrow-line-down"]')

    def enter_buy_pact(self):
        self.driver.click('link', '采购合同')

    def enter_wx_payfor(self):
        self.driver.click('link', '结算管理')
        self. driver.click('link', '外协合同付款')

    def enter_wg_payfor(self):
        self.driver.click('link', '结算管理')
        self.driver.click('link', '外购合同付款')

    def enter_wg_settle(self):
        self.driver.click('link', '结算管理')
        self.driver.click('link', '所有外购合同结算')

    def enter_wx_settle(self):
        self.driver.click('link', '结算管理')
        self.driver.click('link', '所有外协合同结算')

    def add_buy_product_pact(self):
        # 添加购买合同
        self.driver.click('css', '#block6 > div.ibox-title > div > a')

    def add_buy_capacity_pact(self):
        # 添加能力合同
        self.driver.click('css', '#block5 > div.ibox-title > div > a')

    def buy(self):
        # 立刻购买
        self.driver.click('css', '[class="make-order"]')

    def product_inquiry(self):
        # 商品询价
        self.driver.click('class', 'inquiry-order')

    def capacity_inquiry(self):
        # 能力询价
        self.driver.click('class', 'inquiry')

# 我是营销员中的按钮~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def enter_shelf(self):
        self.driver.click_perform('[data-name="zer"]', '[target="_blank"]')


    def enter_market(self):
        # 进入我是营销员
        self.driver.click('link', '我是营销员')
        self.driver.click('css', '[class="btn btn-primary sureBtn"]')

    def shelf_txt(self):
        return self.driver.text('class', 'ht-modal-default-text')

    def surebtn(self):
        self.driver.click('css', '[class="btn btn-primary sureBtn"]')

    def primarybtn(self):
        self.driver.click('css', '[class="btn btn-primary"]')

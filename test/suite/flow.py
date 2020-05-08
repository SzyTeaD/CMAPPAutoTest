import time

from project.cmapp_test.test.suite.button import Button


class Flow():
    def __init__(self,driver):
        self.driver = driver
        self.btn = Button(self.driver)

    def sell_unapprove_flow(self):
        # 卖家不审批
        try:
            self.driver.click('css','[class="btn-primary btn-outline"]')
            self.driver.click('css', '[class="btn btn-primary sureBtn"]')
            self.driver.click('css', '[class="btn btn-primary sureBtn"]')
        except :
            print('卖家不审批失败')
        # self.driver.click_perform('[data-id='+"\""+pact_id+"\""+']', '[class="btn-primary btn-outline"]')


    def buy_unapprove_unsign_flow(self):
        # 买家不审批
        try:
            self.driver.click('css', '[class="btn-primary btn-outline"]')
            self.btn.surebtn()
            self.btn.surebtn()
            time.sleep(2)
            self.driver.click('css', '[class="btn-primary btn-outline"]')
            self.btn.surebtn()
        except :
            print('买家不审批失败')

    def sure_settle_flow(self,pact_num,num=1):
        '''确认收款流程'''
        try:
            if num == 1:
                self.driver.input('name', 'Q_inquirytheme_SL', pact_num)
                time.sleep(1)
                self.driver.click('id', 'searchBtn')
                self.driver.click('link', '确认')
                self.driver.jump_off()
                self.driver.click('id', 'btnPaymentConfirm')
                self.btn.surebtn()
                time.sleep(80)
                self.btn.surebtn()
            else:
                for i in range(int(num) ):
                    self.driver.input('name', 'Q_inquirytheme_SL', pact_num)
                    self.driver.click('id', 'searchBtn')
                    self.driver.click('link', '确认')
                    self.driver.jump_off()
                    self.driver.click('id', 'btnPaymentConfirm')
                    self.btn.surebtn()
                    time.sleep(60)
                    self.btn.surebtn()
        except:
            print('确认收款失败')



    def share_product_flow(self,keyword,address='北京'):
        # 个人商品分享流程
        #self.btn.enter_market(driver)
        self.person_product_center()
        self.product_selecet(keyword,address)
        self.join_shelf()
        time.sleep(1)
        self.btn.enter_shelf()
        self.driver.jump_off()

    def team_share_product_flow(self, keyword, address='北京'):
        '''团队商品分享流程'''
        #self.btn.enter_market()
        self.team_center()
        self.product_selecet(keyword,address)
        self.join_shelf()
        time.sleep(1)
        self.btn.enter_shelf()
        self.driver.jump_off()

    def share_capacity_flow(self, keyword,address='北京'):
        '''个人商品分享流程'''
        #self.btn.enter_market(driver)
        self.person_product_center()
        self.product_selecet(keyword,address)
        time.sleep(1)
        self.driver.click('css', '#capacity > span')
        self.join_shelf()
        self.btn.enter_shelf()
        self.driver.jump_off()
        time.sleep(1)
        self.driver.click('css', '[class="btn btn-white"]')

    def team_share_capacity_flow(self, keyword,address='北京'):
        '''个人能力分享流程'''
        #self.btn.enter_market(driver)
        self.team_center()
        self.product_selecet(keyword,address)
        self.driver.click('id', 'capacity')
        self.join_shelf()
        self.btn.enter_shelf()
        self.driver.jump_off()
        time.sleep(1)
        self.driver.click('css', '[class="btn btn-white"]')


    def add_buy_product_pact_flow(self):
        '''添加个人商品合同流程'''
        self.btn.enter_buy_pact()
        self.btn.add_buy_product_pact()

    def add_buy_capacity_pact_flow(self):
        # 添加个人能力合同流程
        self.btn.enter_buy_pact()
        self.btn.add_buy_capacity_pact()

    def youxuan_flow(self):
        self.driver.click('link', '优选')
        self.driver.jump_off()
        self.driver.click('css', '[class="form-control-radio-icon"]')
        self.driver.click('id', 'btnConfirm')
        try:
            self.btn.surebtn()
        except Exception:
            pass
        self.driver.click('id', 'btnConfirm')
        self.btn.surebtn()

    def payment_flow(self):
        self.driver.click('link', '云端营销')
        self.driver.click('link', '企业兑付管理')

    def join_shelf(self):
        time.sleep(1)
        try:
            #点击加入货架
            self.driver.click('css','body > div.container-cloud > div.container-main.clearfix.open-sidebar > div.main-content > div > div:nth-child(4) > div > div.store-content.hyzx.container > div > div > div:nth-child(1) > div > div.add-shelf.update_left')
            time.sleep(1)
            self.driver.click('css', '[class="btn btn-primary sureBtn"]')
            self.driver.click('id', 'checkShelf')
            # self.driver.click('link', '货架管理')
        except Exception:
            self.driver.click('css', '[class="btn btn-primary sureBtn"]')
            self.driver.click('css','body > div.container-cloud > div.container-main.clearfix.open-sidebar > div.main-content > div > div:nth-child(4) > div > div.store-content.hyzx.container > div > div > div:nth-child(1) > div > div.add-shelf.update_left')
            time.sleep(1)
            self.driver.click('css', '[class="btn btn-primary sureBtn"]')
            self.driver.click('id', 'checkShelf')
            # self.driver.click('link', '货架管理')

    def person_product_center(self):
        # 进入货源中心
        self.driver.click('link', '货源中心')

    def team_center(self):
        self.driver.click('link', '资质申请')
        time.sleep(1)
        self.driver.click('id', 'statusImgTeam')
        self.driver.move_to('class', 'select-text')
        time.sleep(1)
        #driver.click('class', 'select-text') #选择团队
        self.driver.click('id', 'toHYZX')

    def product_selecet(self,keyword, address='北京'):
        # 货源中心搜索
        self.driver.click('link', address)
        self.driver.input('id', 'newKeyword', keyword)
        self.driver.click('class', 'new_search_btn')
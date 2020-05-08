
class ShelfPage(object):
    def __init__(self, driver):
        self.driver = driver

    def add_shelf(self):
        # 添加货架
        self.driver.click('id', 'btnAddNewShelf')

    def delete_shelf(self):
        # 删除货架
        self.driver.click('class', 'btnDeleteShelf')

    def modify_shelf(self):
        # 编辑货架
        self.driver.click('class', 'btnModifyShelf')

    def rename_shelf(self, name):
        # 输入新货架名称
        self.driver.input('name', 'newshelfname', name)
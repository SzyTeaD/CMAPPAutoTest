import os

# url setting
# 测试环境中各个页面网址
TEST_ROOT_URLCONF = 'http://test.cmapp.casicloud.com/'
TEST_SHELF_URL = os.path.join(TEST_ROOT_URLCONF, 'home/cloudmarketing/main/shelflist')
# 正式环境境中各个页面网址
FORMAL_ROOT_URLCONF = 'http://cmapp.casicloud.com/'
FORMAL_SHELF_URL = os.path.join(FORMAL_ROOT_URLCONF, 'home/cloudmarketing/main/shelflist')

# 测试账号
TEST = {
    'MarketerName': '15801590000',
    'MarketerPassword': 'yw123456',
    'BUSR': '600022_system',
    'BPSW': 'yw123456',
    'SUSR': '15801590000',
    'SPSW': 'yw123456',
}
FORMAL = {
    'MarketerName': '15801590000',
    'MarketerPassword': 'yw123456',
    'BUSR': '600022_system',
    'BPSW': 'yw123456',
    'SUSR': '15801590000',
    'SPSW': 'yw123456',
}

# 项目文件路径
BASE_DIR = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]    # 项目的绝对路径
CONFIG_DIR = os.path.join(BASE_DIR, 'config')     # 配置文件路径
PROJECTINFO = os.path.join(CONFIG_DIR, 'projectInfo.yml')
DATA_DIR = os.path.join(BASE_DIR, 'data')     # 测试数据路径
PICTURE_DIR = os.path.join(BASE_DIR, 'picture')   # 图片类文件路径
DRIVER_DIR = os.path.join(BASE_DIR, 'driver')     # 驱动文件根路径
LOG_PATH = os.path.join(BASE_DIR, 'log')     # 日志路径
REPORT_DIR = os.path.join(BASE_DIR, 'report')     # 测试报告路径
CASE_DIR = os.path.join(os.path.join(BASE_DIR, 'test'), 'case')     # 测试用例路径

#
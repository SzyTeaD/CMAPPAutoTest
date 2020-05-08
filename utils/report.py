import os
import unittest

from config.setting import REPORT_DIR, CASE_DIR, DATE
from utils import HTMLTestRunnerCN

def runner(test,caseName):
    discover = unittest.defaultTestLoader.discover(start_dir=CASE_DIR,
                                                   pattern=test)
    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)
    reportpath = os.path.join(REPORT_DIR, DATE + ' %sReport.html' % caseName)
    fp = open(reportpath, 'wb')
    runner = HTMLTestRunnerCN.HTMLTestReportCN(fp)
    runner.run(discover)


if __name__ == '__main__':
    runner('test_clockout*', 'ShelfTest')

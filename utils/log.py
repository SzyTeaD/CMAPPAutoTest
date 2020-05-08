
import os
import logging
from logging.handlers import TimedRotatingFileHandler

from config.setting import LOG_DIR, LOG_CONF, DATE


class Logger(object):
    def __init__(self, caseName):
        self.caseName = caseName
        self.logger = logging.getLogger(self.caseName)
        logging.root.setLevel(logging.NOTSET)
        logSet = LOG_CONF    # 读取日志配置
        if not os.path.exists(LOG_DIR):
            os.mkdir(LOG_DIR)
        self.log_file_name = logSet.get('file_name') if logSet and logSet.get('file_name') else DATE+'test.log'  # 日志文件
        self.backup_count = logSet.get('backup') if logSet and logSet.get('backup') else 5  # 保留的日志数量
        # 日志输出级别
        self.console_output_level = logSet.get('console_level') if logSet and logSet.get('console_level') else 'WARNING'
        self.file_output_level = logSet.get('file_level') if logSet and logSet.get('file_level') else 'DEBUG'
        pattern = logSet.get('pattern') if logSet and logSet.get('pattern') else \
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'    # 日志输出格式
        self.ft = logging.Formatter(pattern)


    def remove_log(self):
        """删除多余日志"""
        while True:
            lists = os.listdir(LOG_DIR)
            log_count = len(set(lists))
            if log_count <= self.backup_count:
                break
            else:
                lists.sort(key=lambda fn: os.path.getmtime(LOG_DIR))
                old_log_file = os.path.join(LOG_DIR, lists[0])
                os.remove(old_log_file)

    def get_logger(self):
        if not self.logger.handlers:  # 避免重复日志
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.ft)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)
            self.remove_log()   # 每天重新创建一个日志文件，最多保留backup_count份
            lf = TimedRotatingFileHandler(filename=os.path.join(LOG_DIR, DATE+' '+self.log_file_name),
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8'
                                                    )
            lf.setFormatter(self.ft)
            lf.setLevel(self.file_output_level)
            self.logger.addHandler(lf)
            # 在控制台输出日志信息
            ls = logging.StreamHandler()
            ls.setFormatter(self.ft)
            ls.setLevel(self.file_output_level)
            self.logger.addHandler(ls)
        return self.logger


if __name__ == '__main__':
    Logger('ShelfTest').get_logger().info('doooo')
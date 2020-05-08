import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config.setting import MAIL_CONF, REPORT_DIR, LOG_DIR, DATE, TIME


class Mail(object):
    def __init__(self, caseName):
        self.caseName = caseName
        self.mailSet = MAIL_CONF
        if not os.path.exists(REPORT_DIR):
            os.mkdir(REPORT_DIR)
        self.senduser = self.mailSet.get('senduser')   # 发送邮箱
        self.sendpswd = self.mailSet.get('sendpswd')   # 授权码
        self.receusers = self.mailSet.get('receusers')  # 收信邮箱

    def new_report(self):
        """筛选出最新的报告"""
        lists = os.listdir(REPORT_DIR)        # 获取路径下的文件
        lists.sort(key=lambda fn: os.path.getmtime(REPORT_DIR))        # 按照时间顺序排序
        new_report = os.path.join(REPORT_DIR, lists[-1])        # 获取最近时间的
        return new_report

    def new_log(self):
        lists = os.listdir(LOG_DIR)
        lists.sort(key=lambda fn: os.path.getmtime(LOG_DIR))
        new_log_file = os.path.join(LOG_DIR, lists[-1])

        new_log = open(new_log_file, 'r', encoding='utf-8').read()
        return new_log

    def remove_mail(self):
        """删除多余邮件"""
        while True:
            lists = os.listdir(REPORT_DIR)
            log_count = len(set(lists))
            if log_count <= 5:
                break
            else:
                lists.sort(key=lambda fn: os.path.getmtime(REPORT_DIR))
                old_log_file = os.path.join(REPORT_DIR, lists[0])
                os.remove(old_log_file)

    def send_mail(self):
        self.remove_mail()
        body_main = self.new_log()
        report = self.new_report()
        msg = MIMEMultipart()
        msg['Subject'] = Header('%s-%s:测试报告' % (self.caseName,DATE,), 'utf-8')   # 邮件标题
        text = MIMEText(body_main, 'html', 'utf-8')  # 邮件内容
        msg.attach(text)
        att = MIMEText(open(report, 'rb').read(), 'base64', 'utf-8')    # 发送附件
        att['Content-Type'] = 'application/octet-stream'
        att.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', DATE + "Report.html"))
        msg.attach(att)
        smtp = smtplib.SMTP()
        smtp.connect('smtp.qq.com')
        smtp.login(self.senduser, self.sendpswd)
        msg['From'] = self.senduser
        for receuser in self.receusers:
            msg['To'] = receuser
            smtp.sendmail(self.senduser, receuser, msg.as_string())


if __name__ == '__main__':
    eml = Mail('Shelftest')
    eml.send_mail()


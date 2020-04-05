import smtplib
from email.mime.text import MIMEText
from email.header import Header



class SendMail(object):

    def __init__(self):
        self.sender = 'feeling@xxx.com'
        self.receivers = ['111111@qq.com']
        # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        self.smtpObj = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
        self.smtpObj.login(self.sender, '72pmarkrWqJx5yyy')
        pass

    def sendMail(self,sendText=''):
        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        self.message = MIMEText(sendText, 'plain', 'utf-8')
        self.message['From'] = Header("牡蛎数据", 'utf-8')  # 发送者
        self.message['To'] = Header("爸爸爸爸", 'utf-8')  # 接收者

        if len(sendText) > 0:
            self.subject = sendText
        else:
            self.subject = 'Python SMTP 数据问题报告'
        self.message['Subject'] = Header(self.subject, 'utf-8')
        try:
            self.smtpObj.sendmail(self.sender, self.receivers, self.message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException as e:
            print(e)
            print("Error: 无法发送邮件")

if __name__ == "__main__":
    c = SendMail()
    c.sendMail('测试，测试，测试数据')

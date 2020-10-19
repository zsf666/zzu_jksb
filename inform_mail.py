# coding=utf-8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import os
import configparser
from email import encoders
from email.mime.base import MIMEBase


class mail:
    def __init__(self):
        proDir = os.path.split(os.path.realpath(__file__))[0]
        configPath = os.path.join(proDir, "config.ini")
        parser = configparser.ConfigParser()
        parser.read(configPath, encoding='UTF-8')
        send_mail = parser.items('sendmail')  # 获取发送邮箱服务器配置
        self.host_server = send_mail[0][1]
        self.sender_qq = send_mail[1][1]
        self.pwd = send_mail[2][1]
        self.sender_qq_mail = send_mail[3][1]
        self.mail_title = send_mail[5][1]

    def mail(self, str, e_mail):
        # qq邮箱smtp服务器

        # 收件人邮箱
        receiver = e_mail
        # 邮件的正文内容
        mail_content = str

        msg = mail_content + '''<html>
        <body>
        <br>
        </br>
        <h1>mail_content</h1>
        <img src="cid:0">
        <img src="cid:1">
        <img src="cid:2">
        </body>
        </html>'''
        # 邮件对象:
        message = MIMEMultipart()
        message.attach(MIMEText(msg, 'html', 'utf-8'))
        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        # message = MIMEText(msg, 'html', 'utf-8')

        message['from'] = self.sender_qq_mail
        message['to'] = receiver
        password = self.pwd
        message['subject'] = Header(u'ZZU健康打卡温馨提示', 'utf-8').encode()
        smtp_server = self.host_server
        server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
        # 打印出和SMTP服务器交互的所有信息。
        # server.set_debuglevel(1)
        # 登录SMTP服务器
        server.login(message['from'], password)

        # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
        with open('./image/IMG1.JPG', 'rb') as f:
            # 设置附件的MIME和文件名，这里是png类型:
            mime = MIMEBase('image', 'jpg', filename='timg.jpg')
            # 加上必要的头信息:
            mime.add_header('Content-Disposition', 'attachment', filename='test.png')
            mime.add_header('Content-ID', '<0>')  # 如果有多个文件需要使用.format(index)
            mime.add_header('X-Attachment-Id', '0')  # 如果有多个文件需要使用.format(index)
            # 把附件的内容读进来:
            mime.set_payload(f.read())
            # 用Base64编码:
            encoders.encode_base64(mime)
            # 添加到MIMEMultipart:
            message.attach(mime)

        # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
        with open('./image/IMG2.JPG', 'rb') as f:
            # 设置附件的MIME和文件名，这里是png类型:
            mime = MIMEBase('image', 'jpg', filename='timg.jpg')
            # 加上必要的头信息:
            mime.add_header('Content-Disposition', 'attachment', filename='test.png')
            mime.add_header('Content-ID', '<1>')  # 如果有多个文件需要使用.format(index)
            mime.add_header('X-Attachment-Id', '1')  # 如果有多个文件需要使用.format(index)
            # 把附件的内容读进来:
            mime.set_payload(f.read())
            # 用Base64编码:
            encoders.encode_base64(mime)
            # 添加到MIMEMultipart:
            message.attach(mime)

        # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
        with open('./image/IMG3.JPG', 'rb') as f:
            # 设置附件的MIME和文件名，这里是png类型:
            mime = MIMEBase('image', 'jpg', filename='timg.jpg')
            # 加上必要的头信息:
            mime.add_header('Content-Disposition', 'attachment', filename='test.png')
            mime.add_header('Content-ID', '<2>')  # 如果有多个文件需要使用.format(index)
            mime.add_header('X-Attachment-Id', '2')  # 如果有多个文件需要使用.format(index)
            # 把附件的内容读进来:
            mime.set_payload(f.read())
            # 用Base64编码:
            encoders.encode_base64(mime)
            # 添加到MIMEMultipart:
            message.attach(mime)
        # 发邮件，由于可以一次发给多个人，所以传入一个list;
        # 邮件正文是一个str，as_string()把MIMEText对象变成str。
        server.sendmail(message['from'], [message['to']], message.as_string())
        server.quit()

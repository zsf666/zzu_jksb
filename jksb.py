#coding=utf-8
import urllib
import json
import requests
import re
from bs4 import BeautifulSoup

from email.mime.text import MIMEText
from email.header import Header
import smtplib
import sys

reload(sys)
sys.setdefaultencoding('utf8')

host = 'jksb.v.zzu.edu.cn'
hea = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
            
            'Host':host}
hea1 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
            'Referer':"https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0",
            'Host':host}
hea2 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
            'Referer':"https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb",
            'Host':host}
hea3 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
            'Referer':"",
            'Host':host}

# 打卡人需要填写的信息，若有多人需要打卡，只需要在user_data中继续创建字典即可
user_data = [
        {   'username':'',  #可填可不填
            'uid':'',       #学号   
            'upw':'',       #登陆密码
            'mail':'',      #邮箱名

    #下列信息需要读者自行登录郑州大学jksb平台，模拟登陆打卡一次，在打卡成功以后在控制台中自行查看填写，其中有些没有信息
            'myvs_13a': '',
            'myvs_13b': '',
            'myvs_13c': '',
            'myvs_14': '',
            'myvs_14b': '',
            'myvs_15': '',
            'myvs_16': '',
            'myvs_16b': '',
            'myvs_17': '',
            'myvs_18': '',
        }]

# 下列信息在程序运行过程中会自动更新，不需要手动填写
post_data = {
    'uid': '',
    'upw': '',
    'smbtn': '进入健康状况上报平台',
    'hh28': '686'
    }
jksb_data = {
    'day6': '',
    'did': '',
    'door':'' ,
    'men6': '',
    'ptopid': '',
    'sid': ''
}
submit_data = {
    'myvs_1': '否',
    'myvs_2': '否',
    'myvs_3': '否',
    'myvs_4': '否',
    'myvs_5': '否',
    'myvs_6': '否',
    'myvs_7': '否',
    'myvs_8': '否',
    'myvs_9': '否',
    'myvs_10': '否',
    'myvs_11': '否',
    'myvs_12': '否',
    'myvs_13a': '',
    'myvs_13b': '',
    'myvs_13c': '',
    'myvs_14': '',
    'myvs_14b': '',
    'myvs_15': '',
    'myvs_16': '',
    'myvs_16b': '',
    'myvs_17': '',
    'myvs_18': '',
    'did': '',
    'door': '',
    'day6': '',
    'men6': '',
    'sheng6': '',
    'shi6': '',
    'fun3': '',
    'ptopid': '',
    'sid': ''
}
user_mail = ''


# 这里SSL验证路径可填服务器本地cert路径，也可选择填写True或False.
verify_path = False
def mail(str):
    #qq邮箱smtp服务器
    host_server = 'smtp.qq.com'
    #sender_qq为发件人的qq号码
    sender_qq = ''
    #pwd为qq邮箱的授权码
    pwd = '' ## xh**********bdc
    #发件人的邮箱
    sender_qq_mail = ''
    #收件人邮箱
    receiver = user_mail

    #邮件的正文内容
    mail_content = str
    #邮件标题
    mail_title = ''

    #ssl登录
    smtp = smtplib.SMTP_SSL(host_server)
    #set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)

    msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = receiver
    smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
    smtp.quit()

# 获取post请求中的ptopid和sid
def re_id(url): 
    # data = url.text
    data = ''.join(url)
    # print(data)
    data = data.split('=')
    sid = data[2]
    ptopid = data[1].split('&')
    ptopid = ptopid[0]
    submit_data['ptopid'] = ptopid
    submit_data['sid'] = sid
    # print(submit_data['ptopid'])
    # print(submit_data['sid'])
    # pattern1 = re.compile(r'ptopid="(.*?)',re.I| re.M)
    # pattern2 = re.compile(r'sid="(.*?)',re.I| re.M)
    # ptopid = pattern1.findall(data)
    # print(ptopid)
    # # sid = pattern2.findall(data) 
    # print(sid)
def re_url(html):
    html.encoding = 'utf-8' #这一行是将编码转为utf-8否则中文会显示乱码。
    
    html = html.text
    soup1 = BeautifulSoup(html,'lxml')
    datas = soup1.find('script')
    datas = datas.string
    pattern = re.compile(r'window.location="(http.*?)"', re.I | re.M)
    # script = datas.get_text()
    # print("script",script)
    url = pattern.findall(datas)
    return url
def re_url1(html):
    html.encoding = 'utf-8' #这一行是将编码转为utf-8否则中文会显示乱码。
    html = html.text
    soup1 = BeautifulSoup(html,'lxml')
    datas = soup1.find('iframe')
    # pattern = re.compile(r'src="(https.*?)"')
    # print(datas)
    # script = datas.get_text()
    url = datas['src']
    # print(url)
    return url

# 判断今日是否填报过
def re_content(html):
    html.encoding = 'utf-8' #这一行是将编码转为utf-8否则中文会显示乱码。
    html = html.text
    soup1 = BeautifulSoup(html,'lxml')
    
    # value = post_data['value']
    # print(value)
    datas = soup1.find('span')
    # pattern = re.compile(r'window.location="(http.*?)"', re.I | re.M)
    datas = datas.string
    datas.encoding = 'utf-8'
    # url = pattern.findall(script)
    if datas=="今日您已经填报过了":
        return False
    else:
        post_data = soup1.findAll('input')
        # print(post_data)
        res = []
        for data in post_data:
            res.append(data['value'])
        jksb_data['day6'] = res[0]
        jksb_data['did'] = res[1]
        jksb_data['door'] = res[2]
        jksb_data['men6'] = res[3]
        jksb_data['ptopid'] = res[4]
        jksb_data['sid'] = res[5]
        submit_data['day6'] = jksb_data['day6']
        submit_data['door'] = jksb_data['door']
        submit_data['men6'] = jksb_data['men6']
        # print(jksb_data)
        return True
def post_url():
    session = requests.Session()
    html = session.post('https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login',  data = post_data,headers = hea1,verify = verify_path)
    url = re_url(html)
    print(url)
    if len(url)>0:
        re_id(url[0])
        return url[0]
    else:
        return 0
def get_url1(url):
    session = requests.Session()
    html = session.get(url,headers = hea,verify = verify_path)
    url = re_url1(html)
    if len(url)>0:
        return url
    else:
        return 0
def get_url2(url):
    session = requests.Session()
    html = session.get(url,headers = hea,verify = verify_path)
    # html.encoding = 'utf-8'
    # html = html.text
    # soup1 = BeautifulSoup(html,'lxml')
    # print(soup1)
    return re_content(html)
def jksb():
    url = "https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb"
    session = requests.Session()
    html = session.post(url,data = jksb_data, headers = hea3,verify = verify_path)
    html = session.post(url,data = submit_data,headers = hea2,verify = verify_path)
    # html.encoding = 'utf-8'
    # html = html.text
    # soup1 = BeautifulSoup(html,'lxml')
    # print(soup1)
    # datas = soup1.findAll('div')
    # print("提取内容:",datas)

if __name__ == '__main__':
    for user in user_data:
        post_data['uid'] = user['uid']
        post_data['upw'] = user['upw']
        submit_data['myvs_13b'] = user['myvs_13b']
        submit_data['myvs_13c'] = user['myvs_13c']
        submit_data['myvs_16b'] = user['myvs_16b']
        submit_data['myvs_17'] = user['myvs_17']
        submit_data['myvs_18'] = user['myvs_18']
        user_mail = user['mail']
        print(mail)
        i = 1
        url = post_url()
        if url != 0:
            # print("first success!")
            url1 = get_url1(url)
            # print(url1)
            if url1 != 0:
                hea3['Referer'] = url1
                if get_url2(url1)== True:
                    jksb()
                    email_message = user['username']+"，今日已成功打卡！"
                    mail(email_message)
                else:
                    # print("Success")
                    email_message = user['username']+"，您今日已经打过卡了！"
                    mail(email_message)
            else:
                # print("second fail")
                mail("打卡失败")
        else:
            # print("打卡失败")
            mail("打卡失败")
#coding=utf-8
import json
import sendmail
import jksb
import time
from smtplib import SMTP_SSL
import sys
import os
import configparser


def init():
    proDir = os.path.split(os.path.realpath(__file__))[0]
    configPath = os.path.join(proDir,"config.ini")
    parser = configparser.ConfigParser()
    parser.read(configPath,encoding='UTF-8')
    delay_time = parser.get('Delay_Time','time')
    time.sleep(int(delay_time))

def read_submitdata_json():
    json_filename = '/Py/zzu_jksb_upgrade/submit_data.json'
    with open(json_filename,encoding='UTF-8') as f:
        submit_data = json.load(f)
    return submit_data

def read_userdata_json():
    json_filename = '/Py/zzu_jksb_upgrade/user_data.json'
    with open(json_filename,encoding='UTF-8') as f:
        user_data = json.load(f)
    return user_data

def read_postdata_json():
    json_filename = '/Py/zzu_jksb_upgrade/post_data.json'
    with open(json_filename,encoding='UTF-8') as f:
        post_data = json.load(f)
    return post_data

def write_postdata_json(uid,upw):
    json_filename = '/Py/zzu_jksb_upgrade/post_data.json'
    post_data = {}
    post_data['uid'] = uid
    post_data['upw'] = uiw
    post_data['smbtn'] = '进入健康状况上报平台'
    post_data['hh28'] = '686'
    with open(json_filename,'w',encoding='UTF-8') as f:
        json.dump(post_data,f)
    return submit_data

if __name__ == '__main__':
    sendmail = sendmail.mail()
    
    submit_data = read_submitdata_json()
    user_data = read_userdata_json()
    for user in user_data:
        init()
        write_postdata_json(user['uid'],user['upw'])
        post_data = read_postdata_json()
        post = jksb.jksb(user,post_data,submit_data)
        e_mail = user['mail']

        url = post.post_url()
        if url != 0:
            url1 = post.get_url1(url)
            if url1 != 0:
                # hea3['Referer'] = url1
                if post.get_url2(url1)== True:
                    post.jksb()
                    email_message = "亲爱的"+user['username']+"，恭喜您今日成功打卡！"
                    sendmail.mail(email_message,e_mail)
                else:
                    email_message = user['username']+"，你今日已经打过卡了，请不要重复打卡！"
                    sendmail.mail(email_message,e_mail)
            else:
                sendmail.mail("打卡失败",e_mail)
        else:
            sendmail.mail("打卡失败",e_mail)
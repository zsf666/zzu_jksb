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
<<<<<<< HEAD
    time.sleep(int(delay_time))

def read_submitdata_json():
    json_filename = '/Py/zzu_jksb_upgrade/submit_data.json'
=======
    return int(delay_time)
    
def get_filepath():
    proDir = os.path.split(os.path.realpath(__file__))[0]
    configPath = os.path.join(proDir,"config.ini")
    parser = configparser.ConfigParser()
    parser.read(configPath,encoding='UTF-8')
    file_path = parser.get('FILE_PATH','file_path')
    return file_path

def read_submitdata_json(file_path):
    json_filename = file_path + 'submit_data.json'
>>>>>>> 02c8b32c58e3004b08e53c1971b8628d2dea487e
    with open(json_filename,encoding='UTF-8') as f:
        submit_data = json.load(f)
    return submit_data

<<<<<<< HEAD
def read_userdata_json():
    json_filename = '/Py/zzu_jksb_upgrade/user_data.json'
=======
def read_userdata_json(file_path):
    json_filename = file_path + 'user_data.json'
>>>>>>> 02c8b32c58e3004b08e53c1971b8628d2dea487e
    with open(json_filename,encoding='UTF-8') as f:
        user_data = json.load(f)
    return user_data

<<<<<<< HEAD
def read_postdata_json():
    json_filename = '/Py/zzu_jksb_upgrade/post_data.json'
=======
def read_postdata_json(file_path):
    json_filename = file_path + 'post_data.json'
>>>>>>> 02c8b32c58e3004b08e53c1971b8628d2dea487e
    with open(json_filename,encoding='UTF-8') as f:
        post_data = json.load(f)
    return post_data

def write_postdata_json(uid,upw):
<<<<<<< HEAD
    json_filename = '/Py/zzu_jksb_upgrade/post_data.json'
=======
    json_filename = file_path + 'post_data.json'
>>>>>>> 02c8b32c58e3004b08e53c1971b8628d2dea487e
    post_data = {}
    post_data['uid'] = uid
    post_data['upw'] = uiw
    post_data['smbtn'] = '进入健康状况上报平台'
    post_data['hh28'] = '686'
    with open(json_filename,'w',encoding='UTF-8') as f:
        json.dump(post_data,f)
    return submit_data

if __name__ == '__main__':
<<<<<<< HEAD
    sendmail = sendmail.mail()
    
    submit_data = read_submitdata_json()
    user_data = read_userdata_json()
    for user in user_data:
        init()
        write_postdata_json(user['uid'],user['upw'])
        post_data = read_postdata_json()
=======
    delay_time = init()
    file_path = get_filepath()
    sendmail = sendmail.mail()
    
    submit_data = read_submitdata_json(file_path)
    user_data = read_userdata_json(file_path)
    for user in user_data:
        time.sleep(delay_time)
        write_postdata_json(user['uid'],user['upw'])
        post_data = read_postdata_json(file_path)
>>>>>>> 02c8b32c58e3004b08e53c1971b8628d2dea487e
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
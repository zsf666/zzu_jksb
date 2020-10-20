#coding = utf-8
import os
import configparser
import sendmail
import json
import inform_mail
import time

def read_userdata_json():
    json_filename = 'user_data.json'
    with open(json_filename,encoding='UTF-8') as f:
        user_data = json.load(f)
    return user_data

fs = open('Inform.txt',encoding='UTF-8')
inform_content = fs.read()
email = inform_mail.mail()
user_data = read_userdata_json()
for user in user_data:
    time.sleep(60)
    e_mail = user['mail']
    email.mail(inform_content,e_mail)

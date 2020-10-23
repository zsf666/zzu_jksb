# coding=utf-8
import json
import sendmail
import jksb
import os
import configparser


def init():
    ProDir = os.path.split(os.path.realpath(__file__))[0]
    ConfigPath = os.path.join(ProDir, "config.ini")
    parser = configparser.ConfigParser()
    parser.read(ConfigPath, encoding='UTF-8')
    delay_time = parser.get('Delay_Time', 'time')
    return int(delay_time)


def get_filepath():
    ProDir = os.path.split(os.path.realpath(__file__))[0]
    ConfigPath = os.path.join(ProDir, "config.ini")
    parser = configparser.ConfigParser()
    parser.read(ConfigPath, encoding='UTF-8')
    file_path = ProDir + '/'
    return file_path


def read_submitdata_json(file_path=get_filepath()):
    json_filename = file_path + 'submit_data.json'
    with open(json_filename, encoding='UTF-8') as f:
        submit_data2 = json.load(f)
    return submit_data2


def read_userdata_json(file_path=get_filepath()):
    json_filename = file_path + 'user_data.json'
    with open(json_filename, encoding='UTF-8') as f:
        user_data2 = json.load(f)
    return user_data2


def read_postdata_json(file_path=get_filepath()):
    json_filename = file_path + 'post_data.json'
    with open(json_filename, encoding='UTF-8') as f:
        post_data2 = json.load(f)
    return post_data2


def write_postdata_json(uid, upw, file_path=get_filepath()):
    json_filename = file_path + 'post_data.json'
    post_data2 = {'uid': uid, 'upw': upw, 'smbtn': '进入健康状况上报平台', 'hh28': '686'}
    with open(json_filename, 'w', encoding='UTF-8') as f:
        json.dump(post_data2, f)


if __name__ == '__main__':
    sendmail = sendmail.mail()
    print('正在读取数据...')
    submit_data = read_submitdata_json()
    print(submit_data)
    user_data = read_userdata_json()
    print('读取数据成功!')
    for user in user_data:
        init()
        print('正在写入数据...')
        write_postdata_json(user['uid'], user['upw'])
        print('写入数据成功!')
        print('正在读取表单...')
        post_data = read_postdata_json()
        print('读取表单成功!')
        post = jksb.jksb(user, post_data, submit_data)
        e_mail = user['mail']

        url = post.post_url()
        if url != 0:
            url1 = post.get_url1(url)
            if url1 != 0:
                # hea3['Referer'] = url1
                if post.get_url2(url1) is True:
                    email_message = post.jksb()
                    print('正在发送邮件...')
                    sendmail.mail(email_message, e_mail)
                    print('打卡成功，消息已发送')
                else:
                    email_message = user['username'] + "，你今日已经打过卡了，请不要重复打卡！"
                    print('正在发送邮件...')
                    sendmail.mail(email_message, e_mail)
                    print('今日已打卡，消息已发送')
            else:
                sendmail.mail("打卡失败", e_mail)
        else:
            sendmail.mail("打卡失败", e_mail)

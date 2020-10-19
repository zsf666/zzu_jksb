# coding = utf-8
import json
import inform_mail


def read_userdata_json():
    json_filename = 'user_data_test.json'
    with open(json_filename, encoding='UTF-8') as f:
        user_data2 = json.load(f)
    return user_data2


fs = open('Inform.txt', encoding='UTF-8')
inform_content = fs.read()
email = inform_mail.mail()
user_data = read_userdata_json()
for user in user_data:
    e_mail = user['mail']
    email.mail(inform_content, e_mail)

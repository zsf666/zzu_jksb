# 郑州大学健康打卡自动上报程序zzu_jksb
## 本程序运行环境Python3(3.7及以下版本，不要用3.8)或2都可
## 运行前请自行pip安装下列库：
  - requests 
  - BeautifulSoup4
## 新的更新
更新上传健康码提醒功能，执行Inform.py脚本即可发邮件提醒您上传健康码，邮件内容放在Inform.txt中，正文内容采用html书写，修改格式时请注意。
## 更新
#### 由于大家已经全部返郑，submit_data信息不再需要个人单独设置，只需完善配置文件中的信息即可
### config.ini文件
###  [sendmail]
sender_qq = admin@test.com\
pwd = bmosoqkybixddhcg\

### [Delay_Time]
设置程序延迟时间，避免IP被封。单位为秒，默认100

### user_data.json配置文件
添加个人信息，姓名学号等，多用户打卡将字典信息复制粘贴即可

## 使用方法
一共需要修改两个文件，config.ini文件里的qq和qq邮箱授权码（授权码在网页版qq邮箱的设置-账户内，开启IMAP/SMTP服务
并且生成授权码），还有一个文件是user_data.json，根据文件内注释填写即可，这个文件内的邮箱是收件人，上述授权码那个
是发件人，可以选择同号发送也可以选择不同的号


将上述地方修改过后直接运行``main.py``即可


在Linux上设置自动定时任务：
首先:
```
cd /etc/cron.d
vim newcronfile
```
newcronfile内容为：
```
SHELL=/bin/bash
PATH=:sbin:/bin:/usr/sbin:usr/bin
MAILTO=root
HOME//root/test/zzu_jksb  #The directory where your program is located
30 0 * * * root python /root/test/zzu_jksb_main.py
```

#### PS：若读者在运行时出现bs4相关错误
请试着将jksb模块中的
```
soup1 = BeautifulSoup(html,'lxml')
```
全部改为：
```
soup1 = BeautifulSoup(html,'html.parser')
```


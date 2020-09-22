# 郑州大学健康打卡自动上报程序zzu_jksb
## 本程序运行环境Python3或2都可
## 运行前请自行pip安装下列库：
  - requests 
  - BeautifulSoup4
## 更新
#### 由于大家已经全部返郑，submit_data信息不再需要个人单独设置，只需完善配置文件中的信息即可
### config.ini文件
###  [sendmail]
host_server = 127.0.0.1\
sender_qq = admin@test.com\
pwd = bmosoqkybixddhcg\
sender_qq_mail = test1@test.com 

### [FILE_PATH]
当前文件所在根目录
file_path = test_path
### [Delay_Time]
设置程序延迟时间，避免IP被封。单位为秒，默认100

### user_data.json配置文件
添加个人信息，姓名学号等，多用户打卡将字典信息复制粘贴即可

## 使用方法
将上述地方修改过后直接运行``main.py``即可


如需要在Linux上设置自动定时任务，请修改crontab.txt内容，将``file_path``改为``main.py``的绝对路径\
然后运行crontab.sh脚本，然后在出现的页面上键入
```
:wq
```
即可


#### PS：若读者在运行时出现bs4相关错误
请试着将jksb模块中的
```
soup1 = BeautifulSoup(html,'lxml')
```
全部改为：
```
soup1 = BeautifulSoup(html,'html.parser')
```


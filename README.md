# 郑州大学健康打卡自动上报程序zzu_jksb
## 本程序运行环境Python3或2都可
## 运行前请自行pip安装下列库：
  - requests 
  - BeautifulSoup4
## 更新
#### 由于大家已经全部返郑，submit_data信息不再需要个人单独设置，只需完善配置文件中的信息即可
###  [sendmail]
host_server = \
sender_qq = \
pwd = \
sender_qq_mail = 


### [Delay_Time]
设置程序延迟时间，单位为秒，默认100

### user_data.json配置文件
添加个人信息，姓名学号等，多用户打卡将复制粘贴即可

#### PS：若读者在运行时出现bs4相关错误
请试着将jksb模块中的
```
soup1 = BeautifulSoup(html,'lxml')
```
全部改为：
```
soup1 = BeautifulSoup(html,'html.parser')
```


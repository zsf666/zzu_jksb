# 郑州大学健康打卡自动上报程序zzu_jksb
## 本程序运行环境Python3(3.7及以下版本，不要用3.8)或2都可
### 若用户没有服务器或者不想使用云函数的，可以切换至action_branch分支下，使用GitHub Action版本的代码。（感谢[Kris451](https://github.com/Kris451)完成对GitHub Action的适配）
注意，python3.8版本的暂时不能用了，请更换回python3.7及以下版本的代码。
## 运行前请自行pip安装下列库：
  - requests 
  - BeautifulSoup4
## 更新2021.09.23
更新填报疫苗接种情况，默认为2针。如有其他情况请自行更改，更改位置为submit_data.json中myvs_26字段，打了几针后面数字改为几。
## 新的更新
更新user_data.json、submit_data.json信息，默认离校状态为**在校**，如您需要改为离校状态，请修改user_data.json中：
~~~
"leave_school":"已离校"
~~~
更新user_data.json信息，默认打卡所在地为河南省**河南省.郑州市**，如您需要打卡地址，请修改user_data.json中：
~~~
"Area_code":"XX" 
"City_code":"XXXX"
"region":"XX"
~~~
Area_code为省划分代码，City_code为省、市划分代码，如河南省为41，河南省郑州市为4101\
您可以通过下面地址查询当地编号：
https://www.axunxun.com/daima/daima-sheng.php?sd=%E6%B2%B3%E5%8D%97%E7%9C%81 \
**region**格式为“**河南省.郑州市**”
## 新的更新
更新上传健康码提醒功能，执行Inform.py脚本即可发邮件提醒您上传健康码，邮件内容放在Inform.txt中，正文内容采用html书写，修改格式时请注意。
## 更新
#### 由于大家已经全部返郑，submit_data信息不再需要个人单独设置，只需完善配置文件中的信息即可
### config.ini文件
###  [sendmail]
host_server = 127.0.0.1\
sender_qq = admin@test.com\
pwd = XXXXXXXXXXXXXXXXXXXXX\
sender_qq_mail = test1@test.com 

### [FILE_PATH]
当前文件所在根目录
file_path = 
（如果使用相对路径则不需要修改这里）

### [Delay_Time]
设置程序延迟时间，避免IP被封。单位为秒，默认100

### user_data.json配置文件
添加个人信息，姓名学号等，多用户打卡将字典信息复制粘贴即可

## 使用方法
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


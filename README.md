# 郑州大学健康打卡自动上报程序zzu_jksb
## 部署到GitHub Action
GitHub Action是GitHub被微软收购后新的集成方案，其本质就是一台小型服务器。
部署方法：克隆本仓库到本地，并按照上述步骤更改相关文件里面地配置，个性信息。qq邮箱及其授权码等。然后将仓库上传到GitHub，并设置仓库为私密，然后转到仓库的设置，在左边的找到actions，选择enable action，这样就激活了action。此时点击一下右上角的star，action就会被触发一次，可以转到action选项卡查看运行状态。以后每天该脚本就会运行一次。

默认的运行时间是早上5点，可以在.github\workflows\jksb,yml文件里面修改，第8行，0 21 * * *，意思是UTC时间21点自动运行，即北京时间5点。可根据自己需要更改。
欢迎交流：yinmoyuATgmail.com（将AT换成@）。

其实可以通过直接fork并在设置中添加secret的方法部署，但是本人不太擅长python，还没完全搞懂原作者的代码。我只做了一小点贡献。

感谢原作者的代码，祝她顺利上岸！

## 本程序运行环境Python3(3.7及以下版本，不要用3.8)或2都可
## 运行前请自行pip安装下列库：
  - requests 
  - BeautifulSoup4
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




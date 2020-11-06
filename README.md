## 郑州大学健康打卡自动上报程序zzu_jksb
### 本程序运行环境Python3.8及以上(3.7及以下见[SunHuaiju/zzu_jksb](https://github.com/SunHuaiju/zzu_jksb))
### 运行前请自行pip安装下列库：
  - requests 
  - BeautifulSoup4

### 使用方法:
  一共需要修改两个文件
  - config.ini

    文件里的qq和qq邮箱授权码（授权码在网页版qq邮箱的设置-账户内，开启IMAP/SMTP服务并且生成授权码）
  - user_data.json

    根据文件内注释填写即可，这个文件内的邮箱是收件人，上述授权码那个是发件人，可以选择同号发送也可以选择不同的号

### 运行:
将上述地方修改过后直接运行``main.py``即可



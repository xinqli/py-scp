# 文件监听自动上传工具

------

由于在本地开发之后还要上传到测试环境，只能通过git做中间转发比较麻烦，就用python写了一个自动监听文件修改并自动上传到服务器的小工具
项目用到的python依赖：

> * paramiko
> * watchdog



注意：截止目前cryptography依赖包不能使用2.6.1 版本，如果版本是2.6则无法使用。需要2.5以下才可用（没试过2.5）
使用pip uninstall cryptography 
安装pip install cryptography==2.4.2

### 操作
> * python scp.py
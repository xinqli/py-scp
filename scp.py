# -*- coding:utf-8 -*-

import os,sys,time
import paramiko
import getpass

from watchdog.observers import Observer
from watchdog.events import *
from FileEventHandler import *
import datetime

if __name__ == "__main__":
    observer = Observer()
# 服务器
ip = ''
port = 22
user = 'root'
password = ''
localDir = '/Users/admin/project/www/scp'
serverDir = '/root'
event_handler = FileEventHandler()
observer.schedule(event_handler, localDir, True)
observer.start()

def upload_to_server(local_dir, server_dir, file, user, password):

    try:
        transport = paramiko.Transport((ip, 22))
        transport.connect(username = user, password = password)

        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(local_dir + '/' +file, server_dir + '/' + file)
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '|上传成功:' + server_dir + '/' + file)
        transport.close()
    except KeyboardInterrupt:
        print(KeyboardInterrupt)


try:
    print('启动自动上传脚本成功.....')
    while True:
        time.sleep(1)

        file_list = event_handler.get_task_list()
        for i in range(0, len(file_list)):
            # print(file_list[i][len(localDir + '\\'):])
            file_list[i] = file_list[i][len(localDir + '/'):]
            # print(file_list[i].split('\\'));
            file = file_list[i].split('/')
            for j in range(0, len(file)):
                if '.idea' in file:
                    print('忽略ide文件')
                    break
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'|开始上传:' + localDir + '／' + file[j])
                upload_to_server(localDir, serverDir, file[j], user, password)
            # print(file)
except KeyboardInterrupt:
    observer.stop()
    observer.join()
    print('用户退出')


























































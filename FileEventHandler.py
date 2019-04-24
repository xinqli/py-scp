# -*- coding:utf-8 -*-

import os,sys,time
import paramiko
import getpass

from watchdog.observers import Observer
from watchdog.events import *

class FileEventHandler(FileSystemEventHandler):
    taskList = [];
    def __init__(self):
        FileSystemEventHandler.__init__(self)
    def on_moved(self, event):
        if not event.is_directory:
            if event.src_path in self.taskList:
                # 将保存的原来的路径替换成现在的
                self.taskList[self.taskList.index(event.src_path)] = event.dest_path
            else:
                # 不再就追加
                self.taskList.append(event.dest_path)

    def on_created(self, event):
        if not event.is_directory and not event.src_path in self.taskList:
            self.taskList.append(event.src_path)

    def on_deleted(self, event):
        if not event.is_directory and event.src_path in self.taskList:
            self.taskList.remove(event.src_path)
    def on_modified(self, event):
        if not event.is_directory and event.src_path in self.taskList:
            self.taskList.append(event.src_path)
    # 每次监听完后返回变更过的文件并重制
    def get_task_list(self):
        ret_list = self.taskList
        self.taskList = []
        return ret_list
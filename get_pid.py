# -*- coding: utf-8 -*-
# @Author: Yan An
# @Date: 2020-07-22 11:16:37
# @Last Modified by: Yan An
# @Last Modified time: 2020-07-22 11:21:48
# @Email: an.yan@intellicloud.ai
import os
import time
import multiprocessing

def sing(num):
	print('sing pid: ', os.getpid())
	print('sing ppid: ', os.getppid())
	for i in range(num):
		print('sing...')
		time.sleep(0.5)

def dance(num):
	print('dance pid: ', os.getpid())
	print('dance ppid: ', os.getppid())
	for i in range(num):
		print('dance...')
		time.sleep(0.5)

if __name__ == '__main__':
	print('pid: ', os.getpid())
	#使用进程类创建进程对象
	sing_process = multiprocessing.Process(target = sing, args = (3, ))
	dance_process = multiprocessing.Process(target = dance, kwargs = {'num': 3})

	#使用进程对象启动任务
	sing_process.start()
	dance_process.start()

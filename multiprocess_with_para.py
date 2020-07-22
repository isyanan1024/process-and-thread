# -*- coding: utf-8 -*-
# @Author: Yan An
# @Date: 2020-07-22 11:01:41
# @Last Modified by: Yan An
# @Last Modified time: 2020-07-22 11:02:35
# @Email: an.yan@intellicloud.ai
import time
import multiprocessing

def sing(num):
	for i in range(num):
		print('sing...')
		time.sleep(0.5)

def dance(num):
	for i in range(num):
		print('dance...')
		time.sleep(0.5)

if __name__ == '__main__':
	#使用进程类创建进程对象
	sing_process = multiprocessing.Process(target = sing, args = (3, ))
	dance_process = multiprocessing.Process(target = dance, kwargs = {'num': 3})

	#使用进程对象启动任务
	sing_process.start()
	dance_process.start()

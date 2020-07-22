# -*- coding: utf-8 -*-
# @Author: Yan An
# @Date: 2020-07-22 10:43:12
# @Last Modified by: Yan An
# @Last Modified time: 2020-07-22 10:46:25
# @Email: an.yan@intellicloud.ai
import time
import multiprocessing

def sing():
	for i in range(3):
		print('sing...')
		time.sleep(0.5)

def dance():
	for i in range(3):
		print('dance...')
		time.sleep(0.5)

if __name__ == '__main__':
	#使用进程类创建进程对象
	sing_process = multiprocessing.Process(target = sing)
	dance_process = multiprocessing.Process(target = dance)

	#使用进程对象启动任务
	sing_process.start()
	dance_process.start()

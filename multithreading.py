# -*- coding: utf-8 -*-
# @Author: Yan An
# @Date: 2020-07-22 15:01:20
# @Last Modified by: Yan An
# @Last Modified time: 2020-07-22 15:03:47
# @Email: an.yan@intellicloud.ai
import time
import threading

def sing(num):
	for i in range(num):
		print('sing...')
		time.sleep(0.5)

def dance(num):
	for i in range(num):
		print('dance...')
		time.sleep(0.5)

if __name__ == '__main__':
	sing_thread = threading.Thread(target = sing, args = (3, ))
	dance_thread = threading.Thread(target = dance, kwargs = {'num': 2})

	sing_thread.start()
	dance_thread.start()
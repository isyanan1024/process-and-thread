# -*- coding: utf-8 -*-
# @Author: Yan An
# @Date: 2020-07-22 15:29:23
# @Last Modified by: Yan An
# @Last Modified time: 2020-07-22 15:31:15
# @Email: an.yan@intellicloud.ai
import time
import threading

def task():
	time.sleep(0.5)
	current_thread = threading.current_thread()
	print(current_thread)

if __name__ == '__main__':
	for i in range(5):
		sub_thread = threading.Thread(target = task)
		sub_thread.start()
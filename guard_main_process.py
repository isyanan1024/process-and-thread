# -*- coding: utf-8 -*-
# @Author: Yan An
# @Date: 2020-07-22 11:28:39
# @Last Modified by: Yan An
# @Last Modified time: 2020-07-22 11:31:24
# @Email: an.yan@intellicloud.ai
import time
import multiprocessing

def work():
	for i in range(10):
		print('工作中...')
		time.sleep(0.2)

if __name__ == '__main__':
	work_process =multiprocessing.Process(target = work)

	#设置守护主进程，主进程退出后子进程直接销毁，不再执行子进程中的代码
	work_process.daemon = True
	work_process.start()

	time.sleep(1)
	print('主程序执行完成了啦')
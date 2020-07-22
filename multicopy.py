# -*- coding: utf-8 -*-
# @Author: Yan An
# @Date: 2020-07-22 11:44:03
# @Last Modified by: Yan An
# @Last Modified time: 2020-07-22 11:51:23
# @Email: an.yan@intellicloud.ai
import os
import shutil
import multiprocessing

def copy_file(source_data, file, target_data):
	print(os.getpid())
	shutil.copy(os.path.join(source_data, file), target_data)

if __name__ == '__main__':
	source_data = '../dai20200511_images_finished'
	target_data = '../copy_test'

	if not os.path.exists(target_data):
		os.mkdir(target_data)

	for file in os.listdir(source_data):
		copy_process = multiprocessing.Process(target = copy_file, args = (source_data, file, target_data))
		copy_process.start()

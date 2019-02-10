#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import logging
import argparse
from sys import exit
###########################################

# 变量声明
logfile = f'{os.path.basename(__file__)}.log'
version = '1.0'

description = '''
Python 测试文件
生成文件夹 test_py_dir
'''
###########################################

# 参数列表
parser = argparse.ArgumentParser(description='这个程序的简介')
parser.add_argument('-v', '--version', action='store_true', help='显示版本并退出')
parser.add_argument('-d', '--desc', action='store_true', help='显示描述并退出')
args = parser.parse_args()

# 日志记录
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# 日志文件，格式，记录级别 INFO
file_handler = logging.FileHandler(logfile)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s')
file_handler.setFormatter(formatter)
# 输出到屏幕的日志, 记录级别 WARNING
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.WARNING)
formatter_simple = logging.Formatter('[%(levelname)s]: %(message)s')
stream_handler.setFormatter(formatter_simple)
# 添加 Handler
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

###########################################

def main() :
	
	# 创建日志目录
	log_dir = os.path.dirname(logfile)
	if not os.path.isdir(log_dir) :
		try :
			os.makedirs(log_dir)
		except :
			print('无法创建日志目录')
			exit()

	# 显示版本并退出
	if args.version :
		print('Version: ', version)
		exit()
	if args.desc :
		print(description)
		exit()

	os.mkdir('test_py_dir')
    # logger.info('这条日志仅被记录到文件')
	# logger.warning('这条日志被记录到文件并输出至屏幕')

if __name__ == '__main__' :
	main()

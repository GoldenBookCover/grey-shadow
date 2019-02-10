#!/usr/bin/env python3
# -*- coding:utf-8 -*-

###########################################

import os
import logging
import argparse
from sys import exit
import re
import time
from datetime import datetime
###########################################

# 变量声明
version = '1.0.4'
logfile = f'/home/{os.path.basename(__file__)}.log'

'''
1.0.1 增加搜索目录判断，现在的正则表达式直接由终端输入了
1.0.2 修改日志文件路径，查找内容记录日志
1.0.3 规范化
1.0.4 开始时间转换为字符
'''
###########################################

# 参数列表
parser = argparse.ArgumentParser(description='这个程序的简介')
parser.add_argument('-v', '--version', action='store_true', help='显示版本并退出')
args = parser.parse_args()

# 日志记录
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# 记录到文件的日志，记录级别 INFO
file_handler = logging.FileHandler(logfile)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('[%(levelname)s]: %(message)s')
file_handler.setFormatter(formatter)
# 输出到屏幕的日志，记录级别 WARNING
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.WARNING)
formatter_simple = logging.Formatter('%(message)s')
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

	# 记录开始时间
	logger.info('====' + str(datetime.fromtimestamp(time.time())) + '====')
	
	reg = re.compile(input('请输入查询的正则表达式：\n'))
	print('查询的正则表达式：', reg)
	
	web_root = input('请输入查找路径，默认为 /usr/share/nginx\n')
	if len(web_root) == 0 :
		web_root = '/usr/share/nginx'
	elif not os.path.isdir(web_root) :
		print('不是目录，请重新输入')
		exit()
	else :
		pass

	# 获取所有网站目录
	website_list = os.listdir(web_root)
	print(website_list)
	time.sleep(3)
	for website in website_list :

		# 遍历网站目录下的所有文件
		for path, dirs, files in os.walk(os.path.join(web_root, website)) :

			# 判断是否是 php 文件
			for file in files :
				if file.endswith('.php') :
					# 逐行读取文件
					with open(os.path.join(path, file), 'r', encoding = 'latin1') as all_lines :
						for line in all_lines :
							# 正则匹配并记录日志
							if reg.search(line) :
								logger.warning(os.path.join(path, file))
								logger.info(line)


if __name__ == '__main__' :
	main()
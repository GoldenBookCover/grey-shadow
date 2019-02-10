#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import re

version = '1.0.2'
'''
1.0 执行时会在当前目录产生大量文件，建议自己创建一个文件夹
1.0.1 重写了正则表达式，更符合 python 规范
1.0.2 增加了 try else 语句
'''

log_file = input ("Which file do you want to analyze?  ")
regex_head = re.compile(r'^---[a-zA-Z0-9]{8}---A--$')
regex_req = re.compile(r'^(GET|POST|HEAD) (.*?) HTTP')
regex_msg = re.compile(r'\[msg "(.*?)"\]')
regex_data = re.compile(r'\[data "Matched Data: (.*?) found within')

def get_mark(line):
	return line[3:11]

def write_to_file(filename, line) :
	f = open(filename, "a")
	try :
		f.write(line + "\n")
	except :
		print("Can't write to " + filename + " : " + line)
	finally :
		f.close()

def main():
	if os.path.isfile(log_file) :
		mark = "0"
		# f = open(log_file, "r", encoding='utf8')
		with open(log_file, encoding='latin1') as all_lines :
			for current_line in all_lines :
				if regex_head.search(current_line) :
					mark = get_mark(current_line)
					print("\n\n----" + mark + "----")
					write_to_file("index.txt", "\n----" + mark + "----")
		
				req = regex_req.search(current_line)
				if req :
					print(req.group(2))
					write_to_file("index.txt", current_line)
		
				msg = regex_msg.findall(current_line)
				if len(msg) > 0 :
					print(msg)
					for i in msg :
						write_to_file("index.txt", "MESS " + i)
		
				data = regex_data.findall(current_line)
				if len(data) > 0 :
					print(data)
					for i in data :
						write_to_file("index.txt", "DATA " + i)
		
				new_log_name = "newlog-" + mark + ".txt"
				try :
					new_log_file = open(new_log_name, "a")
				except :
					print("can't open new log file.")
				else :
					new_log_file.write(current_line)
				finally :
					new_log_file.close()
	else :
		print ("File not found! ")
	
if __name__ == '__main__' :
	main()
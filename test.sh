#!/bin/bash

# 显示版本并退出
if [ "x$1" = "x--desc" ];then
	echo "测试文件，在当前目录生成 a.txt" && exit 0
fi

touch a.txt

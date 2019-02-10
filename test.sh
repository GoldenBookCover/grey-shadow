#!/bin/bash

# 显示版本并退出
if [ "x$1" = "x-v" ];then
	echo "version $version" && exit 0
fi

touch a.txt

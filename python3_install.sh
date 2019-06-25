#!/bin/bash
# Date - 2018-12-08
# Author - CY
# Function - install python3.7.2 
###########################################

logfile="/home/$(basename ${0}).log"
version='3.7.3'
# 用来检验是否已安装
install_path='/usr/local/lib/python3.7'

# 显示版本并退出
if [ "x$1" = "x-v" ];then
	echo "version $version" && exit 0
fi

# log file locates in /home/admin_tools
if [ ! -d $(dirname "$logfile") ];then
    mkdir -p $(dirname "$logfile") || exception '无法创建 $(dirname "$logfile") 目录'
fi
chown root:root $(dirname "$logfile")
chmod 700 $(dirname "$logfile")

# error handling
function exception {
        echo $1
        echo "$1  Terminated." >> "$logfile" 2> /dev/null
        exit 2
}
# log recording
function record {
        echo $1
        echo $1 >> "$logfile" 2> /dev/null
}
# test log file
record "======Started at `date`======" || exception "Cannot create log file."
###########################################

function python3_install {
	yum install gcc gcc-c++ zlib zlib-devel libffi-devel openssl-devel bzip2-devel -y && record "安装依赖的环境" || exception "无法安装依赖的环境"
	wget https://www.python.org/ftp/python/${version}/Python-${version}.tgz && tar zxf Python-${version}.tgz && record "获取 python3 源代码" || exception "获取 python3 源代码失败"
	cd Python-${version} || exception "无法定位 python3 源代码"
	./configure && record "configure 配置成功" || exception "configure 配置失败"
	make && make install && record "安装成功" || exception "安装失败"
	# python 安装好后，确认安装成功
	record "查看 python3 版本"
	record "可能需要重新登入终端，或开启一个新的 bash"
	python3 --version 
	sleep 2
	# Python ${version} 
}

function startup {
	echo "Loading...3..."
	sleep 1
	echo "Loading...2..."
	sleep 1
	echo "Loading...1..."
	sleep 1
}

# Main function here.
startup
if [ -d "$install_path" ];then
	record "$install_path 目录已存在"
else
	python3_install	
fi


###########################################
record "======Finished at `date`======"
echo "Installation log:  $logfile"
exit 0

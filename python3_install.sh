#!/bin/bash
# Date - 2018-12-08
# Author - CY
# Function - install python3.7.4 on CentOS7
###########################################

logfile="/home/$(basename ${0}).log"
version='3.7.4'
# Just check if python3.7.4 is already installed
install_path='/usr/local/lib/python3.7'

# Show version and exit
if [ "x$1" = "x-v" ];then
	echo "version $version" && exit 0
fi

# Create log folder if not existing
if [ ! -d $(dirname "$logfile") ];then
    mkdir -p $(dirname "$logfile") || exception 'Cannot create folder $(dirname "$logfile")'
fi

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
	yum install gcc gcc-c++ zlib zlib-devel libffi-devel openssl-devel bzip2-devel -y && record "Install dependencies" || exception "Cannot install dependencies"
	wget https://www.python.org/ftp/python/${version}/Python-${version}.tgz && tar zxf Python-${version}.tgz && record "Retriving python3 source code" || exception "Retriving python3 source code FAILED"
	cd Python-${version} || exception "Cannot find python3 source code"
	./configure && record "Configured" || exception "Configuration FAILED"
	make && make install && record "Installation success" || exception "Installation FAILED"
	# Check after installation
	record "Check python3 version"
	record "You may need to run a new terminal"
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
	record "$install_path directory already exists"
else
	python3_install	
fi


###########################################
record "======Finished at `date`======"
echo "Installation log:  $logfile"
exit 0

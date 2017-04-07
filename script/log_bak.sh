#!/bin/bash

DATE=$(date +%Y%m%d%H)

if [ ! -d /alidata/logbak/ ];then
mkdir  /alidata/logbak/
fi
name=$(hostname)

for dir in $(ls /alidata/www/ |grep tomcat)
do
	log_dir=/alidata/www/$dir/logs/
	find $log_dir -mtime +5 -type f -name 'catalina-*' |  xargs tar -zcf /alidata/logbak/${dir}${DATE}.tgz
	if [ $? -eq 0 ];then
		find $log_dir -mtime +10 -type f -name 'catalina-*' |  xargs rm -rf
		if [ $? -eq 0 ];then
			/usr/bin/python /data/sh/log_bak_mail.py "${name} Backup 5 days ago file successfully! and Delete files 10 days ago successfully!"
			
		else
			/usr/bin/python /data/sh/log_bak_mail.py "${name} Delete files 10 days ago failed!"
		fi
	else
		/usr/bin/python /data/sh/log_bak_mail.py "${name} Backup 5 days ago file failed!"
	fi
	
	d=$(df -Th | grep "alidata" | awk '{print $6}' |tr -d %)
	if [ ${d} -gt 60 ];then
			find /alidata/logbak/ -mtime +20 -type f -name '*.tgz' |  xargs rm -rf
	fi

done


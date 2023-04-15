#!/bin/bash
export ORI_WORK_DIR=$(pwd)
export CODE_HOME=$(cd `dirname $0`; pwd)
cd $CODE_HOME


`ps -ef|grep -v grep|grep 'df_spider/main.py'|awk '{print $2}'|xargs kill -9 &> /dev/null`

if [ `ps -ef |grep -v grep |grep 'df_spider/main.py'| wc -l` -gt 0 ]
then echo "服务器df_spider: 服务停止失败"
else echo "服务器df_spider: 服务已停止"
fi


#!/bin/sh
export PRO_NAME=df_spider
export CODE_HOME=$(cd `dirname $0`; pwd)


$CODE_HOME/stop.sh

if [ `echo $?` -ne 0 ]
then echo "服务器${PRO_NAME}: 重启失败" && exit 1
fi

$CODE_HOME/start.sh

if [ `echo $?` -ne 0 ]
then echo "服务器${PRO_NAME}: 重启失败" && exit 1
else echo "服务器${PRO_NAME}: 重启成功"
fi

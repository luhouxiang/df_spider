#!/bin/bash
export ORI_WORK_DIR=$(pwd)
export CODE_HOME=$(cd `dirname $0`; pwd)
cd $CODE_HOME
cd ..
nohup python3 df_spider.py >/dev/null &
PIDS=$!
echo $PIDS > $CODE_HOME/df_spider.pid
if [ `ps -fP $PIDS | wc -l` -gt 1 ]
then echo "服务器df_spider.py: 服务已启动"
else echo "服务器df_spider.py: 服务启动失败"
fi


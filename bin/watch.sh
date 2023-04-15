#!/bin/sh
export ORI_WORK_DIR=$(pwd)
export CODE_HOME=$(cd `dirname $0`; pwd)
cd $CODE_HOME

curday=`date +%Y%m%d`;
log_file='df_spider-'$curday
echo $curday;



tail -f $CODE_HOME/../log/${log_file}.log

cd $ORI_WORK_DIR

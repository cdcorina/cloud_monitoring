#!/bin/bash
DIRS="/var/log /tmp"

for dir in $DIRS
do
    count=$(ls $dir | wc --lines)
    if [ $count -lt 50 ] ; then
        status=2
        statustxt=CRITICAL
    elif [ $count -lt 100 ] ; then
        status=2
        statustxt=CRITICAL
    else
        status=0
        statustxt=OK
    fi
    echo "$status Filecount_$dir count=$count;50;100;0; $statustxt - $count files in $dir"
done

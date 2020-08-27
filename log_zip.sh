#!/bin/bash

logdir=/root/cron_log/
gzip_time=30
mov_time=50

cd $logdir
echo "cd $logdir"
list="deletefile wtest log_zip check_daemon cron_check"
for i in $list
do
    #/usr/bin/find ./ -type f -name "*.log" -mmin +$gzip_time -exec /usr/bin/tar {} \; 2> /dev/null
    #zip script
    /usr/bin/find ./ -type f -name "$i"_'*'.log -mmin +$gzip_time -exec /usr/bin/tar -cvzf $i'_'$(date "+%Y%m%d%H%M").tar.gz $i"*".log {} \; 2> /dev/null
    
    /usr/bin/find ./ -type f -name "$i"_'*'.log -mmin +$gzip_time -exec /usr/bin/mv {} $i'_'*.log /root/_trash \; 2> /dev/null

    #trash move script
    if /usr/bin/ls -lt | /usr/bin/find ./ -mmin +$mov_time | /usr/bin/grep $i
    then
        /usr/bin/find ./ -type f -name "$i"_'*'.log -mmin +$mov_time -exec /usr/bin/mv {} $i'_'*.log /root/_trash \; 2> /dev/null
        
        /usr/bin/find ./ -type f \( -name "$i"_'*'.tar.gz -o -name "$i*.gz" \) -mmin +$mov_time -exec /usr/bin/mv {} $i'_'*.tar.gz /root/_trash \; 2> /dev/null
fi

#echo $i'_'$(date "+%Y%m%d%H%M")
#echo /usr/bin/find ./ -type f -name "$i"_""*".log"
#echo /usr/bin/find ./ -type f -name "$i"_""*".log" -mmin +$gzip_time -exec /usr/bin/tar -cvf $i'_'$(date "+%Y%m%d%H%M").tar $i    "_""*".log {} \; 2> /dev/null
#echo $i"_"*.log
done
        
#/usr/bin/gzip *_date+"%Y%m%d%H%M"-d "-10 minute".log {} \; 2> /dev/null
#/usr/bin/find ./ -type f -name "*.gz" -mmin +$mov_time -exec /usr/bin/mv *.gz/ /root/_trash {} \; 2> /dev/null

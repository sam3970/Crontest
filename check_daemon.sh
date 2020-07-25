#!/bin/sh

#while [ 1 ]

#do
function daemon_check()
{
    #telegram=$(ps -ef | grep bin/telegram | grep -v grep | cut -c59-71 | wc -l)
    mysql=$(netstat -nlp |grep 3306 | awk '{print $4}' | sed 's/::://g')
	httpd=$(netstat -nlp |grep 80 | awk '{print $4}' | sed 's/::://g')
	
	#echo $mysql
	#echo $httpd
	telegram=$(ps -ef | grep telegram | grep -v grep | awk '{print $8}' | sed -n 's|/root/tele/telegram_cli/bin/telegram-cli|telegram|p'|wc -l)
	if [ "${mysql}" = 3306 ] || [ "${telegram}" = 0 ] || [ "${mysql}" = 80 ]
	then
		#if [[ "$count" -eq '0' ]] 
    
	#if [[ "$count" -eq 'telegram' ]] 
		#then
		#echo "daemon(서비스)이 꺼져있어서 daemon(서비스)을 재시작 합니다."
        
        #/root/tele/telegram_cli/bin/telegram-cli -k tg-server.pub restart
        #source /root/crontest/teletime.sh
        return 1
        #cd /usr/local/daemon/bin; ./daemon
    else
        return 2
    fi
    
    sleep 1
}

daemon_check
ttt="$(daemon_check)"
echo $ttt
#done
: << "END"
function mysql_check()
{
	mc = $(netstat -nlp |grep 3306 | awk '{print $4}' | sed 's/::://g')

	if [ "$mc" -eq '3306' ]
	then
		return 1
	else
		return 2
	fi
}
#END

daemon_check
result=$?
echo $result
#echo rt
#$a=tele_check

if [[ "$result" -eq '1' ]]
then
    #export TEXT="daemon(서비스)이 꺼져있어서 daemon(서비스)을 재시작 합니다."
    /root/tele/telegram_cli/bin/telegram-cli -k tg-server.pub &
    echo "daemon(서비스)이 꺼져있어서 daemon(서비스)을 재시작 합니다."
    #sh teletime.sh
    #source /root/crontest/teletime.sh
else
    #export TEXT="daemon(서비스)이 정상적으로 작동중!"
    #sh teletime.sh
    #source /root/crontest/teletime.sh
    echo "daemon(서비스)이 정상적으로 작동중!"
	#echo "통과"
fi
#echo $(a)
END

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os
import sys
import shutil
import string
import psutil
#import requests
#from urllib.parse import urlencode
from datetime import time,datetime
import timeExport #외부파일(timeExport.py)

#dirPath = '/root/_trash';
#savePath = subprocess.check_output("/usr/bin/w | grep root | awk '{{print $1}}'", shell=True)
#command = os.system('w | grep root')

#Path Read
savePath = os.popen("/usr/bin/w | awk '{print $1}'| sort").read();
array=[savePath]

#Server_Name settings
serverName = 'sklee_02'
title = '[' + serverName + ' wtest.py]\r\n'
msg = title

#Message Destination Settings
#def send(chat):
#    print(chat)
#    params1 =  urlencode({'chat_id': '921889996', 'text': chat}).encode()
#    r = requests.post('https://api.telegram.org/bot937768411:AAFbP6he1iZtWpTNvfAVutv_TdO8vSdMk2g/sendMessage',  params=params1, json=[])
#    print(r.elapsed.total_seconds())
#    print(r.json())

#root test script
def root_test():
    for check_dir in array:
        if 'root' in savePath:
	        try:
        	    #for root, dirs, files in os.walk(dirPath):
                	#for f in files:
                        #os.unlink(os.path.join(root, f))
                	#for d in dirs:
                        #shutil.rmtree(os.path.join(root,
                        #msg += "PATH : " + str(savePath) + "w test check passed! %\r\n"
                        p = 'passed!'
                        print(p)
                        #test = os.popen("/usr/bin/ps -fu $array| awk '{print $2}'").read()
                        #print(test)
                        return p;
                        #send(msg)

	        except Exception as ex:                 
                    #msg += "PATH : " + str(savePath) + "w test check failed! %\r\n"
                    print('not exist file and directory!\n')
                    os.system('mkdir /root/_trash');
                    #send(msg)
                    #os.popen("ps -fu USERNAME | awk '{print $2}'").read();

        else:
            print("check to w\n");
            pkill = os.popen("% /usr/bin/kill -9 /usr/bin/ps -fu 'savePath' | awk '{print $2}'").read();
            print(pkill)
            
            msg += "ServerName : " + str(serverName) + " 의심 프로세스 KILL 완료!! \r\n"
            timeExport.send(msg)

#return value saved
rtest = root_test();
#print(rtest)

#for date alarm
#morning = time(8, 00)
#lunchs = time(12, 00)
#lunche = time(13, 00)
#evening = time(18, 00)
#now = datetime.now().time()
dt = datetime.now()

#telegram message send part
if rtest == 'passed!' :
    if timeExport.morning <= timeExport.now and timeExport.evening > timeExport.now :
        if not(timeExport.lunchs <= timeExport.now and timeExport.lunche > timeExport.now) :
            if not(dt.strftime('%A') == 'Saturday' and dt.strftime('%A') == 'Sunday') : #영어로 된 요일 문자열
                #msg += "ServerName : " + str(serverName) + " 에서 테스트 통과!! \r\n"
                #timeExport.send(msg)
                 print('통과!')
else :
    msg += "ServerName : " + str(serverName) + " 서버의 실행유무를 확인해주세요!! \r\n"
    timeExport.send(msg)

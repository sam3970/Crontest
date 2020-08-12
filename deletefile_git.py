#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#created by sam3970

import subprocess
import os
import sys
import shutil
import string
import psutil
#import requests
#from urllib.parse import urlencode
from datetime import time,datetime
import timeExport

dirPath = '/root/_trash';

#Server_Name settings
serverName = 'sklee_02'
title = '[' + serverName + ' deletefile.py]\r\n'
msg = title 


#delete file script part
def delete():
    try : 
        if(os.path.isdir(dirPath)):
            for root, dirs, files in os.walk(dirPath):
                for f in files:
                    os.unlink(os.path.join(root, f))
                for d in dirs:
                    shutil.rmtree(os.path.join(root, d))
            p1 = '1'
            print("completed remove file and directory!")
            return p1
        else :
            p2 = '2'
            os.system('mkdir /root/_trash')
            return p2
    except Exception as ex:                 
        #msg += "PATH : " + str(savePath) + "w test check failed! %\r\n"
        print('Exception occured!\n', ex)
        #os.system('mkdir /root/_trash');
        #send(msg)

#delete definition
delete = delete();
#print(delete)

#for date alarm
#morning = time(8, 00)
#lunchs = time(12, 00)
#lunche = time(13, 00)
#evening = time(18, 00)
#now = datetime.now().time()
dt = datetime.now()

#teletram message send part
#if delete  == '0' :
#    msg += " Servername : " + str(serverName) + " 파일이 존재하지 않음! \r\n"
#    send(msg)

if delete == '1' :
    if timeExport.morning <= timeExport.now and timeExport.evening > timeExport.now :
        if not(timeExport.lunchs <= timeExport.now and timeExport.lunche > timeExport.now) :
            if not(dt.strftime('%A') == 'Saturday' and dt.strftime('%A') == 'Sunday') :
                if delete == '1' :
                    #msg += " Servername : " + str(serverName) + " 에서 파일 및 폴더 삭제 완료! \r\n"
                    #timeExport.send(msg)
                    print("통과!")

                elif delete == '2' :
                    msg += " Servername : " + str(serverName) + " 폴더가 없어서 새로 만듦! \r\n"
                    timeExport.send(msg)

                else :
                    msg += " Servername : " + str(serverName) + " 이상한 값이 반환 됨 체크 필요! \r\n"
                    timeExport.send(msg)

else :
    msg += "ServerName : " + str(serverName) + " 에서 삭제 실패 체크 필요!! \r\n"
    timeExport.send(msg)

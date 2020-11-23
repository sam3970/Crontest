#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import string
import psutil
import subprocess
import requests
from urllib.parse import urlencode

class Health :

	#def __init__(self) :
		#self.cpuLimit = 15; #cpu 사용량
		#self.memLimit = 15; #memory 사용량
		#self.memUsage = memUsage;
		#self.avgCpu = avgCpu;

	# 기준 및 초기값 설정
	cpuLimit = 15 # cpu 사용량
	memLimit = 15 # 메모리 사용량


	serverName = 'sklee_02'
	title = '[' + serverName + ' server]\r\n'
	msg = title

	def send(self,chat):
		print(chat)
		params1 =  urlencode({'chat_id': '921889996', 'text': chat}).encode()
		r = requests.post('https://api.telegram.org/bot937768411:AAFbP6he1iZtWpTNvfAVutv_TdO8vSdMk2g/sendMessage',  params=params1, json=[])
		print(r.elapsed.total_seconds())
		print(r.json())

	# cpu 사용율 계산
	def getCpuUsage(self):
		cpu = 0
		for x in range(2):
			cpu += psutil.cpu_percent(interval=1)
			return round(float(cpu)/3,2)

	# memory 사용량 계산
	def getMemUsage(self):
		mem=str(os.popen('free -t -m').readlines())
		T_ind=mem.index('T')
		mem=mem[T_ind+6:]
		mem_T=mem[:13]
		mem_sub=mem[14:]
		mem_U=mem_sub[:13]
		return round(float(mem_U)/float(mem_T)*100,2)

	#print(memUsage)
	#print(avgCpu)

heal = Health()

memUsage = heal.getMemUsage()
avgCpu = heal.getCpuUsage()

#print(memUsage)

if avgCpu > heal.cpuLimit:
	heal.msg += 'cpu(' + str(heal.cpuLimit) + '%) exceed!.\r\n'
	heal.msg += 'cpu usage : ' + str(avgCpu) + '%\r\n'
	
if memUsage > heal.memLimit:
	heal.msg += 'memory(' + str(heal.memLimit) + '%) exceed!.\r\n'
	heal.msg += 'memory usage : ' + str(memUsage) + '%'
	
if avgCpu > heal.cpuLimit or memUsage > heal.memLimit:
	heal.send(heal.msg)
	
else:
	print("CPU, Memory가 정상수치를 유지하고 있습니다.")

########## main method check part(similar initializing) ##########
#if __name__ == "__main__" :
#    main()

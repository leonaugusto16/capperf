#!/usr/bin/env python
from httperfpy import Httperf
import sys
import string
import re

nm_cnns=1
def init():

	svr="localhost"
	prt=80
	nm_clls=1	
	rcv_bffr=16384	
	snd_bffr=4096
	ur="/"

	i=1
	while i < len(sys.argv): 
		if(sys.argv[i] == "--server"):
			i+=1
			svr=sys.argv[i]
		elif(sys.argv[i] == "--port"):
			i+=1
			prt=sys.argv[i]
		elif(sys.argv[i] == "--num-conns"):
			i+=1
			nm_cnns=sys.argv[i]
		elif(sys.argv[i] == "--num-calls"):
                        i+=1
                        nm_clls=sys.argv[i]
		elif(sys.argv[i] == "--uri"):
                        i+=1
                        ur=sys.argv[i]
		elif(sys.argv[i] == "--recv-buffer"):
                        i+=1
                        rcv_bffr=sys.argv[i]
		elif(sys.argv[i] == "--send-buffer"):
                        i+=1
                        snd_bffr=sys.argv[i]
		elif(sys.argv[i] == "--rage"):
                        i+=1
		else:
			print "WARN: Variable not exist "+sys.argv[i]
			i+=1
		i+=1
		
	perf = Httperf(server=svr,port=prt,num_conns=nm_cnns, num_calls=nm_clls, uri=ur,recv_buffer=rcv_bffr,send_buffer=snd_bffr)
	perf.parser=True
	results = perf.run()

	return results
	print results["connection_time_avg"] + " is avg"
	#print results["connection_time_max"] + " is max"
	#print results["reply_status_3xx"]

def status(results):	
	if(string.atoi(results["reply_status_4xx"]) > 0):
		print "ERROR: "+results["reply_status_4xx"]+" replays code 4xx"
	elif(string.atoi(results["reply_status_3xx"]) > 0):
		print "WARN: "+results["reply_status_3xx"]+" replays code 3xx"
	elif(string.atoi(results["reply_status_2xx"])>0):
		print "OK: "+results["reply_status_2xx"]+" replays code 2xx"

def cap():

	# Primeiro teste
	results = init()
	
	# Proximos testes
	MAX=1000
	s = results["command"].split()
	try:
		result = re.match ('(--num-conns=)(...)', s[7])
		conn = string.atoi(result.group(2))
	except:
		result = re.match ('(--num-conns=)(..)', s[7])
		conn = string.atoi(result.group(2))
	
	MIN = conn
	while MIN < MAX:
		comand = results["command"]
		MIN+=conn
		comand = comand.replace('--num-conns='+str(conn),'--num-conns='+str(MIN))
		perf = Httperf(comand)
		perf.parser=True
        	results = perf.run()
		print results["connection_time_avg"] + " is avg"

cap()

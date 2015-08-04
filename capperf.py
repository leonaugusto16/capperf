#!/usr/bin/env python
from httperfpy import Httperf
import sys

def init():

	svr="localhost"
	prt=80
	nm_cnns=1
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
		else:
			print "WARN: Variable not exist "+sys.argv[i]
			i+=1
		i+=1
		
	perf = Httperf(server=svr,port=prt,num_conns=nm_cnns, num_calls=nm_clls, uri=ur,recv_buffer=rcv_bffr,send_buffer=snd_bffr)
	perf.parser=True
	results = perf.run()

	print results["connection_time_avg"] + " is avg"
	print results["connection_time_max"] + " is max"
	print results["reply_status_3xx"]

init()

#perf = Httperf(server="webmail.dcc.ufrj.br",port=80,num_conns=100)
# replace dashes ("-") with underscores ("_") in httperf options

#perf.parser = True

#results = perf.run()


#print results["connection_time_avg"] + " is avg"
#print results["connection_time_max"] + " is max"
#print results["reply_status_3xx"]

#!/usr/bin/env python
from httperfpy import Httperf
import json,string

def status(self):
        if(string.atoi(self["reply_status_4xx"]) > 0):
                print "[*] ERROR: "+self["reply_status_4xx"]+" replays code 4xx"
        elif(string.atoi(self["reply_status_3xx"]) > 0):
                print "[*] WARN: "+self["reply_status_3xx"]+" replays code 3xx"
        elif(string.atoi(self["reply_status_2xx"])>0):
                print "[*] OK: "+self["reply_status_2xx"]+" replays code 2xx"
	print "\n"

def error(self):
	if(string.atoi(self["errors_addr_unavail"]) > 0):
                print "[*] ERROR: errors_addr_unvail =  "+self["errors_addr_unvail"]
	if(string.atoi(self["errors_ftab_full"]) > 0):
                print "[*] ERROR: errors_ftab_full =  "+self["errors_ftab_full"]
	if(string.atoi(self["errors_conn_reset"]) > 0):
                print "[*] ERROR: errors_conn_reset =  "+self["errors_conn_reset"]
	if(string.atoi(self["errors_client_timeout"]) > 0):
                print "[*] ERROR: errors_client_timeout =  "+self["errors_client_timeout"]
	if(string.atoi(self["errors_conn_refused"]) > 0):
                print "[*] ERROR: errors_conn_refused =  "+self["errors_conn_refused"]
	if(string.atoi(self["errors_fd_unavail"]) > 0):
                print "[*] ERROR: errors_fd_unavail =  "+self["errors_fd_unavail"]


def simple_result(self):
	print "\n[-] Results\n"
	status(self)
	error(self)	

	

def main():
	print "[*] Import data"
	data = json.loads(open('data.json').read())

	print "\n[*] Test in site "+data['server']
	print "[*] Port : "+str(data['port'])
	print "[*] Number calls : "+str(data['num_calls'])
	print "[*] Number connections : "+str(data['num_conns'])
	print "[*] URI : "+str(data['uri'])+"\n"
	perf = Httperf(server=data['server'],port=data['port'],num_conns=data['num_conns'], num_calls=data['num_calls'],uri=data["uri"])

	perf.parser = True

	results = perf.run()

	if(data['result'] == 'simple'):
		simple_result(results)

	return results


if __name__ == '__main__':
	print main()


#!/usr/bin/env python
from httperfpy import Httperf
import json

def simple_result(self):
	

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
	return results


if __name__ == '__main__':
	print main()


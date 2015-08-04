#!/usr/bin/env python
from httperfpy import Httperf

perf = Httperf(server="webmail.dcc.ufrj.br",
port=80,
num_conns=100)
# replace dashes ("-") with underscores ("_") in httperf options

perf.parser = True

results = perf.run()

print results["connection_time_avg"] + " is avg"
print results["connection_time_max"] + " is max"


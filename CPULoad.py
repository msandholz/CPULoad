#!/usr/bin/env python
#coding: utf8

# Import modules
import sys
import os


# Read CPU

import subprocess
command = "top -d 0.1 -b -n2 | grep 'Cpu(s)' | tail -n1"
proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
cpuload = 100-float(out.split(",")[3][1:-3])

print "program output:", out.split(",")[3]

print cpuload

exit()

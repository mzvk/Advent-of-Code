#!/usr/bin/env python

import sys, time

#registers:
a = 0
b = 0

iset = {
  'hlf': lambda x: x/2,
  'tpl': lambda x: x*3,
  'inc': lambda x: x+1,
  'jmp': 0,
  'jie': 0,
  'jio': 0,
}

#    jmp offset is a jump; it continues with the instruction offset away relative to itself.
#    jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
#    jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).

data_in = sys.argv[1] if len(sys.argv[1:]) > 0 else 'inputs/set01/aoc23.in'

def parser(ins, *args):
   print "{} -> {}".format(ins, args)

def load(file):
  with open(file) as x: output = x.read()
  return [line for line in output.split('\n') if line]

def solve(data):
  ip = 0
  result = [0, 0]
  while(ip < len(data)):
#    print "{:02} instruction: {}".format(ip, data[ip])
    if data[ip][:3] == 'jmp': ip = max(0, ip + int(data[ip][4:]))
    else: ip += 1
    print ip
    time.sleep(1)
  print "Pt1: {}\nPt2: {}".format(result[0], result[1])

solve(load(data_in))

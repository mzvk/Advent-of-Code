#!/usr/bin/env python

import sys, time

data_in = sys.argv[1] if len(sys.argv[1:]) > 0 else 'inputs/set01/aoc23.in'

def load(file):
  with open(file) as x: output = x.read()
  return [line for line in output.split('\n') if line]

def solve(data, regs):
  ip = 0
  while(ip < len(data)):
    tokens = [x.replace(',','') for x in data[ip].split()]
    if   (tokens[0] == 'hlf'):
      regs[tokens[1]]/=2
      ip+=1
    elif (tokens[0] == 'tpl'):
      regs[tokens[1]]*=3
      ip+=1
    elif (tokens[0] == 'inc'):
      regs[tokens[1]]+=1
      ip+=1
    elif (tokens[0] == 'jmp'): ip+=int(tokens[1].replace('+',''))
    elif (tokens[0] == 'jio'): ip+=int(tokens[2].replace('+','')) if regs[tokens[1]] == 1 else 1
    elif (tokens[0] == 'jie'): ip+=1 if regs[tokens[1]] % 2  else int(tokens[2].replace('+',''))
  return regs

data=load(data_in)
print "Pt1: {}\nPt2: {}".format(solve(data, {'a': 0, 'b': 0})['b'],solve(data, {'a': 1, 'b': 0})['b'])

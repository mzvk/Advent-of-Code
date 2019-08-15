#!/usr/bin/env python

import sys

data_in = sys.argv[1] if len(sys.argv[1:]) > 0 else 'inputs/set01/aoc12.in'

def load(file):
  with open(file) as x: output = x.read()
  return output.replace('\n', '')

def ifnum(char):
   try:
      return (int(char)^int(char))+1  ## for the negative and 0 values
   except ValueError: return 0

def sgen(input, ptr=0):
   (seq, seqt, neg) = ('', 0, 0)
   while ptr < len(input):
      if input[ptr] == '"': seqt ^= 1
      elif input[ptr] == "-": neg = 1
      elif ifnum(input[ptr]) or seqt: seq += input[ptr]
      elif seq:
         ptr -= 1
         yield seq if not neg else "-"+seq
         (seq, neg) = ('', 0)
      else: yield input[ptr]
      ptr += 1

def parse(input, ot=0, bv=0, bve=0):
   ign = 0
   bvt = bve
   for char in input:
      if char in ['{','[']:
         (bv, bve) = parse(input, 1 if char == '{' else 0, bv, bve)
      elif char in ['}', ']']:
         return (bv, bvt if ign else bve)
      else:
         if ifnum(char):
            bv  += int(char)
            bve += int(char)
         elif char == "red" and ot: ign = 1
   return (bv, bve)

def solve(input):
   result = parse(sgen(input))
   print "Pt1: {}\nPt2: {}".format(result[0], result[1])

solve(load(data_in))

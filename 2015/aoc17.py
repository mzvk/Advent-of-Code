#!/usr/bin/env python

import sys

eggnog = 150
low = 150
data_in = sys.argv[1] if len(sys.argv[1:]) > 0 else 'inputs/set01/aoc17.in'

def load(file):
   with open(file) as x: output = x.read()
   return sorted([int(x) for x in output.split('\n') if x], reverse=True)

#first-fit decreasing algorithm
def firstfit(idx=0, capa=0, total=0, totallow=0, elnu=0):
   global low
   for glass in cntnr[idx:]:
      if glass + capa == eggnog:
         if(elnu+1 == low): totallow += 1
         elif(elnu+1 < low):
            totallow = 1
            low = elnu+1
         total += 1
      elif glass + capa < eggnog:
         (total, totallow) = firstfit(idx+1, capa+glass, total, totallow, elnu+1)
      idx += 1
   return (total, totallow)

def solve(input):
   global cntnr
   cntnr = input
   result = firstfit()
   print "Pt1: {}\nPt2: {}".format(result[0], result[1])

solve(load(data_in))

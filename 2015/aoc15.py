#!/usr/bin/env python

import sys, re
from functools import reduce

data_in = sys.argv[1] if len(sys.argv[1:]) > 0 else 'inputs/set01/aoc15.in'

def gen_mix(ingc,total):
   beg = max(total, 1) if ingc == 1 else 1
   for i in range(beg, total + 1):
      if ingc - 1:
         for y in gen_mix(ingc - 1, total - i):
            yield [i] + y
      else:
         yield [i]

def load(file):
  properties = []
  with open(file) as x: output = x.read()
  for line in output.split('\n'):
     ingr = re.search(r'^[A-Z][a-z]+: [a-z]+ (-?[0-9]+), [a-z]+ (-?[0-9]+), [a-z]+ (-?[0-9]+), [a-z]+ (-?[0-9]+), [a-z]+ (-?[0-9]+)$', line)
     if ingr: properties.append([int(ingr.group(x)) for x in xrange(1, 6)])
  return properties

def score(ingr, stats):
   if len(ingr) != len(stats): return 0
   iscore = []
   for x in xrange(len(stats[0]) - 1):
      iscore.append(max(reduce(lambda x,y: x+y, [i[0] * i[1] for i in zip(ingr, [s[x] for s in stats])]), 0))
   return max(reduce(lambda x,y: x * y, iscore), 0)

def calories(ingr, stats):
   return reduce(lambda x,y: x+y, [x[0]*x[1] for x in zip(ingr, [i[4] for i in stats])])

def solve(data):
  result = [0, 0]
  for v in gen_mix(len(data), 100):
     result[0] = max(score(v, data), result[0])
     if calories(v, data) == 500: result[1] = max(score(v, data), result[1])
  print "Pt1: {}\nPt2: {}".format(result[0], result[1])

solve(load(data_in))

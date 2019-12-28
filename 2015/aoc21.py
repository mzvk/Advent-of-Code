#!/usr/bin/env pyton

import sys, re

PC = {'hp': 100, 'at': 0, 'df': 0}
BC = {'hp': 0, 'at': 0, 'df': 0}

eql = [[[8 , 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]],
      [[13, 0, 1],  [31, 0, 2], [53, 0, 3], [75, 0, 4], [102,0, 5]],
      [[25, 1, 0],  [50, 2, 0], [100,3, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3]]]

data_in = sys.argv[1] if len(sys.argv[1:]) > 0 else 'inputs/set01/aoc21.in'

class regex(object):
  def __or__(self, other):
    self.sre = other
    return other
  def group(self, index=0):
    return self.sre.group(index)

def load(file):
  rgx = regex()
  with open(file) as x: output = x.read()
  for line in output.split('\n'):
    if rgx|re.match(r'Hit Points: ([0-9]+)', line): BC['hp'] = int(rgx.group(1))
    if rgx|re.match(r'Damage: ([0-9]+)', line): BC['at'] = int(rgx.group(1))
    if rgx|re.match(r'Armor: ([0-9]+)', line): BC['df'] = int(rgx.group(1))

def max_price(eql, mp=0):
   for idx, eqll in enumerate(eql):
      mp += max(x[0] for x in eqll)
      if idx == 2: mp += sorted([x[0] for x in eqll], reverse=True)[1]
   return mp

def combinations(*list):
   comblist = [[]]
   for lst in map(tuple, list):
      comblist = [x+[y] for x in comblist for y in lst]
   for comb in comblist:
      yield comb

def update_stats(EQ):
   PC['at'] = 0
   PC['df'] = 0
   cost = 0
   for idx, itm in enumerate(EQ):
      if itm == -1: continue
      if idx == 3: idx = 2
      PC['at'] += eql[idx][itm][1]
      PC['df'] += eql[idx][itm][2]
      cost += eql[idx][itm][0]
   return cost

def calc_dmg(at, df):
   return at - df if at - df > 0 else 1

def solve(data):
   load(data)
   comb_gen = combinations(xrange(-1, len(eql[0])), xrange(-1, len(eql[1])), xrange(-1, len(eql[2])), xrange(-1, len(eql[2])))
   result = [max_price(eql), 0]

   for eq in comb_gen:
     if eq[0] == -1 or eq[2] == eq[3]: continue
     cost = update_stats(eq)
     if (BC['hp']//calc_dmg(PC['at'],BC['df']) + (1 if BC['hp']%calc_dmg(PC['at'],BC['df']) else 0) <=
         PC['hp']//calc_dmg(BC['at'],PC['df']) + (1 if PC['hp']%calc_dmg(BC['at'],PC['df']) else 0)):
        result[0] = min(cost, result[0])
     else:
        result[1] = max(cost, result[1])

   print "Pt1: {}\nPt2: {}".format(result[0], result[1])

solve(data_in)

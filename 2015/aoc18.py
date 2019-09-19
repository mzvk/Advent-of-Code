#!/usr/bin/env python

import sys, copy

data_in = sys.argv[1] if len(sys.argv[1:]) > 0 else 'inputs/set01/aoc18.in'
MAX_EPOCH = 100
_GRIDX = 100 ## defualt
_GRIDY = 100 ## default

newborns = {}

def load(file):
  global _GRIDX, _GRIDY
  with open(file) as x: output = x.read()
  size = output.split('\n')
  (_GRIDX, _GRIDY) = (len(size[0]), len([line for line in size if line]))
  flock = [idx for idx, pos in enumerate(output.replace('\n','')) if pos == '#']
  return flock

def solve(data, immortals, epoch_max, epoch=0):
  global newborns
  flock = {k:[1,0] for k in (data + immortals)}
  while(epoch < epoch_max):
    new_flock = {}
    newborns = {}
    for cell in flock:
      if cell >= _GRIDX * _GRIDY: continue
      flock[cell][1] = countN(cell, flock)
      if (flock[cell][1] >= 2 and flock[cell][1] <= 3) or cell in immortals: new_flock[cell] = [1,0]
    for cell in newborns:
      if newborns[cell] == 3: new_flock[cell] = [1,0]
    flock = copy.deepcopy(new_flock)
    epoch += 1
  return len(flock)

def countN(cell, flock):
   neighbors = set([-_GRIDX+1,-_GRIDX,-_GRIDX-1,+1,_GRIDX+1,_GRIDX,_GRIDX-1,-1])
   result = 0
   if(cell / _GRIDY == 0):          neighbors -= {-_GRIDX-1, -_GRIDX, -_GRIDX+1} ## upper
   if(cell / _GRIDY == _GRIDY - 1): neighbors -= { _GRIDX-1,  _GRIDX,  _GRIDX+1} ## lower
   if(cell % _GRIDX == 0):          neighbors -= {-_GRIDX-1,      -1,  _GRIDX-1} ## leftmost
   if(cell % _GRIDX == _GRIDX - 1): neighbors -= {-_GRIDX+1,       1,  _GRIDX+1} ## righmost

   for neighbor in neighbors:
     if neighbor + cell in flock: result += 1
     else: newborns[neighbor + cell] = newborns[neighbor + cell] + 1 if neighbor + cell in newborns else 1
   return result

result = [solve(load(data_in), [], MAX_EPOCH), solve(load(data_in), [0, _GRIDX-1, _GRIDX*(_GRIDY-1), _GRIDX*_GRIDY-1], MAX_EPOCH)]
print "Pt1: {}\nPt2: {}".format(result[0], result[1])

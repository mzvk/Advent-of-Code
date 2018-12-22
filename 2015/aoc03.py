#!/usr/bin/env python

data_in = 'inputs/aoc03.in'

act={'<': lambda x: [x[0] - 1, x[1]], '>': lambda x: [x[0] + 1, x[1]], '^': lambda x: [x[0], x[1] + 1], 'v': lambda x: [x[0], x[1] - 1]}

def load(file):
  with open(file) as x: output = x.read()
  return output.replace('\n', '')

def solve(data):
  p1 = set()
  p2 = set()
  (rsp, sp, nsp) = ([0, 0], [0, 0], [0, 0])

  for idx, mv in enumerate(data):
    sp = act[mv](sp)
    p1.add("{}:{}".format(sp[0], sp[1]))

    if idx % 2:
      rsp = act[mv](rsp)
      p2.add("{}:{}".format(rsp[0], rsp[1]))
    else:
      nsp = act[mv](nsp)
      p2.add("{}:{}".format(nsp[0], nsp[1]))

  print "Pt1: {}\nPt2: {}".format(len(p1), len(p2))

solve(load(data_in))

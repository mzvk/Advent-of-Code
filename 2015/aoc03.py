#!/usr/bin/env python

data_in = 'inputs/aoc03.in'

act={'<': lambda x: [x[0] - 1, x[1]], '>': lambda x: [x[0] + 1, x[1]], '^': lambda x: [x[0], x[1] + 1], 'v': lambda x: [x[0], x[1] - 1]}

def load(file):
  with open(file) as x: output = x.read()
  return output.replace('\n', '')

def move(pos, mv, cache):
  pos = act[mv](pos)
  cache.add("{}:{}".format(pos[0], pos[1]))
  return (pos, cache)

def solve(data):
  (p1, p2) = (set(), set())
  (rsp, sp, nsp) = ([0, 0], [0, 0], [0, 0])

  for idx, mv in enumerate(data):
    (sp, p1) = move(sp, mv, p1)

    if idx % 2:
      (rsp, p2) = move(rsp, mv, p2)
    else:
      (nsp, p2) = move(nsp, mv, p2)

  print "Pt1: {}\nPt2: {}".format(len(p1), len(p2))

solve(load(data_in))

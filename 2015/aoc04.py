#!/usr/bin/env python

import hashlib, sys, os

data_in = sys.argv[1] if len(sys.argv[1:]) > 0 else 'inputs/set01/aoc04.in'
gensfx = lambda s = 0: (str(s + 1*x) for x, _ in enumerate(iter(int, 1)))

def load(file):
  with open(file) as x: output = x.read()
  return output.replace('\n', '')

def solve(data):
  progress = '\|/-\|/-'
  output = [0, 0]
  for sufix in gensfx():
    if(hashlib.md5("{}{}".format(data, sufix)).hexdigest()[:5] == '0' * 5 and not output[0]): output[0] = sufix
    if(hashlib.md5("{}{}".format(data, sufix)).hexdigest()[:6] == '0' * 6 and not output[1]): output[1] = sufix
    if(output[0] and output[1]):
      sys.stdout.write("\rPt1: {n1:{width}}\nPt2: {n2:{width}}".format(n1=output[0], n2=output[1], width=len(sufix)))
      sys.stdout.flush()
      return 0
    sys.stdout.write("\r [{}] {}".format(progress[int(sufix) % 8], sufix))
    sys.stdout.flush()

try:
  os.system('setterm -cursor off')
  solve(load(data_in))
finally:
  os.system('setterm -cursor on')

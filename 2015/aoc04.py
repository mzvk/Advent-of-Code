#!/usr/bin/python

import hashlib, threading, sys

data_in = sys.argv[1] if len(sys.argv[1:]) > 0 else 'inputs/set01/aoc04.in'
tcount = 128
output = [0, 0]
gensfx = lambda s = 0, y = 1: (s + y*x for x, _ in enumerate(iter(int, 1)))

class dohash(threading.Thread):
  def __init__(self, offset, data):
    threading.Thread.__init__(self)
    self.offset = offset
    self.data = data
  def run(self):
    for sufix in gensfx(self.offset, tcount):
      hash = hashlib.md5("{}{}".format(self.data, sufix)).hexdigest()
      if hash[:5] == '0' * 5:
        if not output[0]: output[0] = sufix
        elif sufix < output[0]: output[0] = sufix
      if hash[:6] == '0' * 6:
        if not output[1]: output[1] = sufix
        elif sufix < output[1]: output[1] = sufix
      if (output[0] and sufix > output[0]) and (output[1] and sufix > output[1]): break

def load(file):
  with open(file) as x: output = x.read()
  return output.replace('\n', '')

def solve(data):
  gLock = threading.Lock()
  try:
    threads = [dohash(tid, 'yzbqklnj') for tid in xrange(tcount)]
    [t.start() for t in threads]
  except:
    print "Unable to start threads"
  [t.join() for t in threads]
  print "Pt1: {}\nPt2: {}".format(output[0], output[1])

solve(load(data_in))

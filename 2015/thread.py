#!/usr/bin/python

import thread, hashlib, sys

tcount = 128
output = [0, 0]
gensfx = lambda s = 0, y = 1: (str(s + y*x) for x, _ in enumerate(iter(int, 1)))

def print_time(offset, data):
   for sufix in gensfx(offset, tcount):
      hash = hashlib.md5("{}{}".format(data, sufix)).hexdigest()

      if hash[:5] == '0' * 5:
        if not output[0]: output[0] = sufix
        elif int(sufix) < int(output[0]): output[0] = sufix

      if hash[:6] == '0' * 6:
        if not output[1]: output[1] = sufix
        elif int(sufix) < int(output[1]): output[1] = sufix

      if output[0] and output[1]: break

try:
   tidl = [thread.start_new_thread(print_time, (tid, 'yzbqklnj')) for tid in xrange(tcount)]
except:
   print "Error: unable to start thread"

while 1:
  if output[0] and output[1]:
    print "Pt1: {}\nPt2: {}".format(output[0], output[1])
    break

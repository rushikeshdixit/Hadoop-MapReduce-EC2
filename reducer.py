#!/usr/bin/env python

from operator import itemgetter
import sys

carrier_delay = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    #print line
    try:
    # parse the input we got from mapper.py
        carrier, delay = line.split('\t')
    #  convert count (currently a string) to int
        delay = float(delay)
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
        if not carrier in carrier_delay:
           carrier_delay[carrier] = []
        carrier_delay[carrier].append(delay)
    except:
        continue

for carrier in carrier_delay:
    len_values = len(carrier_delay[carrier])
    carrier_delay[carrier] = sum(carrier_delay[carrier])/len_values
    print '%s, %s' % (carrier, carrier_delay[carrier])

#!/usr/bin/env python

import sys
headerPresent = True
#input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
	if headerPresent:
		headerPresent = False
		continue
    	line = line.strip()
    # split the line into words
    	line = line.split(",")
    # increase counters
	if line>=2:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        	word=line[9]
		word1=line[15]
		print '%s\t%s' % (word, word1)

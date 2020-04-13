# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:03:30 2020

@author: vinic_000
"""

original = "python2_lesson14_keys_.pkl"
destination = "python2_lesson14_keys.pkl"

content = ''
outsize = 0
with open(original, 'rb') as infile:
    content = infile.read()
with open(destination, 'wb') as output:
    for line in content.splitlines():
        outsize += len(line) + 1
        output.write(line + str.encode('\n'))

print("Done. Saved %s bytes." % (len(content)-outsize))
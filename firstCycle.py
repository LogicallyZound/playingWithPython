# find a cycle in a sequence of numbers from a file

import sys

def fc(lsOfSeqs):
  for ls in lsOfSeqs:
     swag = {}
     for i,k in enumerate(ls):
        if(k in swag):
        #  print ls
        #  print "printing range: ", 0, "to", 4
           print ' '.join(ls[swag[k]:i])
           break
        else: swag[k] = i



test_cases = open(sys.argv[1], 'r')
with test_cases as f:
   #numbers = [ [line 1]  line 2[]  [line 3]]
   numbers = [map(str, l.split()) for l in f]
fc(numbers)


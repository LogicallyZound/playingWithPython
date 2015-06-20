import sys
test_cases = open(sys.argv[1], 'r')

with test_cases as f:
   numbers = [map(str, l.split()) for l in f]

def rw(lss):
   for ls in lss:
      print ' '.join(ls[::-1]),
      print "\n",
   

rw(numbers)

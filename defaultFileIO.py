#
#

import sys




test_cases = open(sys.argv[1], 'r')
with test_cases as f:
   #numbers = [ [line 1]  line 2[]  [line 3]]
   numbers = [map(int, l.split()) for l in f]


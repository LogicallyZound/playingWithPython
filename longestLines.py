# print out n longest lines in a file

import sys
test_cases = open(sys.argv[1], 'r')

with test_cases as f:
   numbers = [map(str, l.split()) for l in f]

numLines = int(''.join(numbers[0]))

def ll(strls):
   maxlen = 0
   for s in strls:
      tlen = len(' '.join(s))
      if ( tlen > maxlen ):
         maxlen = tlen 
#         print "New maxlength is: ", maxlen
   return maxlen

def p(n,strls, ml):
   while n != 0:
      for s in strls:
         if (len(' '.join(s)) == ml):
            if(n != 0):
               print ' '.join(s)
               n -= 1
      ml = ml-1

p(numLines, numbers[1:len(numbers)], ll(numbers[1:len(numbers)]) )





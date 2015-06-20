import sys
test_cases = open("testFB.txt")

with test_cases as f:
   numbers = [map(int, l.split()) for l in f]

def fb(X, Y, n):
   for x in range(1, n+1):
      if ((x % X == 0) and (x % Y == 0)):
         print 'FB',
      elif (x % X == 0):
         print 'F',
      elif (x % Y == 0):
         print 'B',
      else:
         print x,
   print '\n',

for ls in numbers:
   fb(ls[0], ls[1], ls[2])

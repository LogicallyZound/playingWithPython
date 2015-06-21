import sys
#prints out the FIBNUM'th fib number

F = [0,1]
FIBNUM = 50

def fib():
   print F[0]
   print F[1]
   for i in range(2, FIBNUM):
      F.append(F[i-2] + F[i-1])
      print F[i] 

fib()

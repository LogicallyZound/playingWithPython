s = 0;
nu = 0;

for num in range(2, 100000):
   if nu != 1000:
      for i in range(2, num):
         if(num % i) == 0: 
            break
      else:
         nu += 1;
#         print "added: ", nu, " numbers together"
         s += num
   else: break

print s


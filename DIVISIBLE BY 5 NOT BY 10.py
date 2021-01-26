lower = 5
upper = int(input("Enter upper range limit:"))
for i in range(lower, upper+1):
   if(i%5==0) & (i%10!=0):
      print(i)

R=int(input("Enter the number if Red squares: "))
B=int(input("Enter the number if Blue squares: "))
if(abs(R-B)!=1):
   print("Not Possible")
else:
   if(R>B):
      for i in range(min(R,B)):
         if(R>B):
            print("RB",end="")
         else:
            print("BR",end="")
      if(R>B):
         print("R")
      else:
         print("B")

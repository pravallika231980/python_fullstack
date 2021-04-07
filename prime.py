num=int(input("enter the value:"))
if num>1:
   if num==2:
      print("number is prime")
   for i in range(2,num):
      if num%i==0:
         print("Given number is not prime")
         break    
      else:
         print("it is  prime number")
         break     
else:
   print("Given number is not prime number")
         
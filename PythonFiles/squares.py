#d=dict()
#n=int(input("enter the range:"))
#for i in range(1,n+1):
 # d[i]=i*i
#print(d)
def square(min,max):
  d=dict()
  for i in range(min,max+1):
    d[i]=i*i
  print(d)
square(1,10)

  
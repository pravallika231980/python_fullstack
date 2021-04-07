def even(min,max):
  l1=[]
  for i in range(min,max+1):
    if(i%2)==0:
      print("even numbers are:")
      l1.append(str(i))
  print(' '.join(l1))
even(1000,3000)
      
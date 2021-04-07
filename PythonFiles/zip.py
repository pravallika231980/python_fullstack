fruits=["apple","banana","cherry"]
colors=['red','yellow','pink']
for i,x in zip(fruits,colors):
   print(i,x)
l1,l2=zip(*[('apple','red'),('banana','yellow'),('cherry','pink')])
print(l1,l2)
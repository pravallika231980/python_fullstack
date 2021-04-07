import math
c=50;h=30
q=[]
items=[i for i in input().split(',')]
for d in items:
  q.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print(','.join(q))


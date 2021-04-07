r=int(input("enter no of rows:"))
c=int(input("enter no of columns:"))
x=[[int(input()) for i in range(c)] for j in range(r)]
r=int(input("enter no of rows:"))
c=int(input("enter no of columns:"))
y=[[int(input()) for i in range(c)] for j in range(r)]
result=[]
for i in range(r):
  for j in range(c):
    print(x[i][j],end=" ")
  print()
for i in range(r):
  for j in range(c):
    print(y[i][j],end=' ')
  print()
for i in x:
  for j in y:
    for k in y:
      result[i][j]+=x[i][k]*y[k][j]
for r in result:
  print(r)
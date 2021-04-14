from functools import reduce
"""Print squares Using lambda function with syntax:lambda arguments:expression"""
lambda_square=list(map(lambda x:x**2,[1,2,3,4,5]))
print(lambda_square)
"""Printing odd numbers using Filter() whoich return true stmts as a list"""
l1=[1,2,3,4,5,6,7,8,9]
l1=list(filter(lambda y:(y%2)!=0,l1))
print(l1)
"""Pring sum of list usin reduce along with lambda which takes two arguments"""
l2=[1,2,3,4,5,6]
l2=reduce((lambda x,y:x+y),l2)
print(l2)
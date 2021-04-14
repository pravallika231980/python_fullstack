from functools import partial
# def f(a,b,c,x):
#     return 1000*a+100*b+10*c+x
# g=partial(f,1,1,1)
# print(g(5))
def add(a,b,c):
    return a+b+c
a=partial(add,1,2)
print(a(3))
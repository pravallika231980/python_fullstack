"""This is generation function to print fibonacci numbers"""
def fibgenfun(limit):
    a,b=0,1
    while a<limit:
        yield a
        a,b=b,a+b
x=fibgenfun(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
for i in fibgenfun(5):
    print(i)
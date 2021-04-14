# def exgen(limit):
#     a=0
#     while a<limit:
#         yield a
#         a+=1
# for i in exgen(5):
#     print(i)
def gensquare(limit):
    a=1
    while True:
        yield a*a
        a+=1
for i in gensquare(5):
    if i<100:
        print(i)
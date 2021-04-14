"""This is A class"""
class A:
    """This is A class Constructor with X variable"""
    def __init__(self,x):
        print("this is a class method")
        self.x=x
        """Ths is B subclass derived from A class"""
class B(A):
    """This is A class Constructor with X  and Y variable"""
    def __init__(self,x,y):
        """THIS is super() to access base class method"""
        super().__init__(x)
        print("This is B Class Method")
        self.y = y
        """This is print() to print X,y Arguments"""
    def printXY(self):
        print(self.x,self.y)
"""Initialization of derived class B"""
obj=B(10,20)
print(obj)
print(obj.printXY())

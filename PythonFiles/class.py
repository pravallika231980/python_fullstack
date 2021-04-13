"""This is class """
class Iofun():
    """This is a constructor class with no argument"""
    def __init__(self):
        self.st=""
        """THIS IS a method with no argument to print the string"""
    def getString(self):
        self.st=input("enter the string:")
        """this is a method to print th"e string"""
    def printString(self):
        print(self.st.upper())
k=Iofun()
k.getString()
k.printString()


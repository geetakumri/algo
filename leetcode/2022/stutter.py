"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
"""


class InputString:
    def __init__(self):
        pass
        # self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())


strInput = InputString()
strInput.getString()
strInput.printString()

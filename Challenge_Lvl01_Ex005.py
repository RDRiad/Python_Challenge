
"""
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""


class RDInputOutput(object):

    def __init__(self):
        self.s = ""

    def input_Fun(self):
        self.s = str(input("entre a str: "))

    def output_Fun(self):
        print(self.s.upper())

RDClass = RDInputOutput()
RDClass.input_Fun()
RDClass.output_Fun()

# Q4
#
# Define a class StringReader which has at least two methods:
# inputString: to get a string from console input
# printStringUpper: to print the string in upper case
#
# The object should have one property string which holds the
# current value of the string.
#
# The method printStringUpper should first check if string
# is already defined. If it is not, it should print the statement
# "string is uninitialized"
#
# Hint:
# Make use of the built-in hasattr() and input() function

class StringReader:

    def inputString(self):
        self.string = input("Please enter string > ")

    def printStringUpper(self):
        if not hasattr(self, 'string'):
            print("string is uninitialized")
        print(self.string)

sr = StringReader()
sr.printStringUpper()

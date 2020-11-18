from read import *
from write import *
from delete import *
import sys

# This class has a constructor and 3 methods which call imported functions inside them.

class NotePad:

    def __init__(self, filename): 
        self.filename = filename
    def ReadNotePad(self):
        read(self.filename)

    def WriteNotePad(self):
        write(self.filename)

    def DeleteNotePad(self):
        delete(self.filename)

if __name__ == "__main__":

    myNotePad = NotePad("file.txt")
    choice = ""
    while choice != "exit":
        choice = input("What would you like to do: \n  (Type 1 to read, 2 to write and 3 to delete) \n")
        if choice == '1':
            myNotePad.ReadNotePad()
        elif choice == '2':
            myNotePad.WriteNotePad()
        elif choice == '3':
            myNotePad.DeleteNotePad()
        else:
            sys.exit()

from tkinter import *
import random


class Generator:
    def __init__(self):
        self.window = Tk()
        self.window.title("Password Generator")
        self.window.geometry("500x500")

        self.includeUpper = IntVar()
        self.includeNumber = IntVar()
        self.includeSymbol = IntVar()

        self.U = Checkbutton(self.window, text = "Uppercase", variable = self.includeUpper)
        self.N = Checkbutton(self.window, text = "Number", variable = self.includeNumber)
        self.S = Checkbutton(self.window, text = "Symbols", variable = self.includeSymbol)

        self.U.pack()
        self.N.pack()
        self.S.pack()

        generate = Button(self.window, text = "Generate Password", command = self.generatePass)
        generate.pack()

        self.passText = StringVar()
        password = Label(self.window, textvariable = self.passText, relief = GROOVE)
        password.pack()

        self.copy = Button(self.window, text = "Copy", command = self.copyToClipboard)
        self.copy.pack()

        mainloop()

    def generatePass(self):
        self.lowerChar = "abcdefghijklmnopqrstuvwxyz"
        self.upperChar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.numberChar = "1234567890"
        self.symbolChar = "[]{}()*;/,.-_"

        self.allChar = self.lowerChar

        self.allChar += self.upperChar if self.includeUpper.get() == 1 else self.allChar
        self.allChar += self.numberChar if self.includeNumber.get() == 1 else self.allChar
        self.allChar += self.symbolChar if self.includeSymbol.get() == 1 else self.allChar
        
        self.passLength = 12
        self.password = "".join(random.sample(self.allChar, self.passLength))
        print(self.password)
        self.passText.set(str(self.password))

    def copyToClipboard(self):
        self.window.clipboard_clear()
        self.window.clipboard_append(self.password)

    

my_gui = Generator()

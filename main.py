from tkinter import *
import random

class Generator:
    def __init__(self):
        # Window setup
        self.window = Tk()
        self.window.title("Password Generator")
        self.window.geometry("400x400")
        self.window.minsize(400, 400)
        self.window.maxsize(400, 400)

        #Settings
        settingsLabel = Label(self.window, text = "SETTINGS")
        settingsLabel.place(x = 10, y = 10)

        # Checkbox to include Uppercase, Numbers and Symbols
        self.includeUpper = IntVar()
        self.includeNumber = IntVar()
        self.includeSymbol = IntVar()
        self.U = Checkbutton(self.window, text = "Uppercase", variable = self.includeUpper)
        self.N = Checkbutton(self.window, text = "Number", variable = self.includeNumber)
        self.S = Checkbutton(self.window, text = "Symbols", variable = self.includeSymbol)
        self.U.place(x = 10, y = 30)
        self.N.place(x = 10, y = 50)
        self.S.place(x = 10, y = 70)

        # Password length
        self.lengthLabel = Label(self.window, text = "Length")
        self.lengthLabel.place(x = 10, y = 108)
        self.passLength = IntVar(value = 10)
        self.lengthSlider = Scale(self.window, variable = self.passLength, from_ = 1, to = 32, orient = HORIZONTAL)
        self.lengthSlider.place(x = 60, y = 90)

        # Use custom character?
        self.useCustomChar = IntVar()
        self.customChar = Checkbutton(self.window, text = "Use Custom Characters", variable = self.useCustomChar, command = self.useCustomCharacters)
        self.customChar.place(x = 200, y = 30)

        # Custom character inputs
        self.custChar = StringVar()
        self.customInput = Entry(self.window, textvariable = self.custChar, state = DISABLED)
        self.customInput.place(x = 225, y = 50)

        # Generate Password Button
        generate = Button(self.window, text = "Generate Password", command = self.generatePass)
        generate.place(x = 150, y = 270)

        # Display Password
        passwordLabel = Label(self.window, text = "Password: ")
        passwordLabel.place(x = 10, y = 300)
        self.passText = StringVar()
        password = Label(self.window, textvariable = self.passText, relief = GROOVE)
        password.place(x = 70, y = 300, width = 250)

        # Copy Password Button
        self.copy = Button(self.window, text = "Copy", command = self.copyToClipboard)
        self.copy.place(x = 325, y = 297)

        mainloop()

    # Function to generate password based on the settings
    def generatePass(self):
        # Default settings
        self.lowerChar = "abcdefghijklmnopqrstuvwxyz"
        self.upperChar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.numberChar = "1234567890"
        self.symbolChar = "[]{}()*;/,.-_"

        self.allChar = self.lowerChar

        # Check settings
        if (self.useCustomChar.get() == 0):
            self.allChar += self.upperChar if self.includeUpper.get() == 1 else self.allChar
            self.allChar += self.numberChar if self.includeNumber.get() == 1 else self.allChar
            self.allChar += self.symbolChar if self.includeSymbol.get() == 1 else self.allChar
        else:
            self.allChar = ""
            for i in range(int(self.passLength.get()/len(self.custChar.get()))+1):
                self.allChar += self.custChar.get()

        # Generate Password
        self.password = "".join(random.sample(str(self.allChar), int(self.passLength.get())))
        self.passText.set(str(self.password))

    # Function to copy password to clipboard
    def copyToClipboard(self):
        self.window.clipboard_clear()
        self.window.clipboard_append(self.password)

        # Display text for 0.5 second
        self.copyLabel = Label(self.window, text = "Copied!")
        self.copyLabel.place(x = 170, y = 320)
        self.copyLabel.after(500, self.copyLabel.destroy)
    
    def useCustomCharacters(self):
        if (self.useCustomChar.get() == 1):
            self.U.config(state = DISABLED)
            self.N.config(state = DISABLED)
            self.S.config(state = DISABLED)
            self.customInput.config(state = NORMAL)
        else:
            self.U.config(state = ACTIVE)
            self.N.config(state = ACTIVE)
            self.S.config(state = ACTIVE)
            self.customInput.config(state = DISABLED)
            

    
my_gui = Generator()

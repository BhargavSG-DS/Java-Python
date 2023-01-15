# Slip7_2B
import string,random
from tkinter import *


class PasswordGenetorGUI:
    def __init__(self):
        self.gui = Tk()
        self.gui.configure(background = "lightblue")
        self.gui.title("Slip7_2B")
        self.gui.geometry("325x150")

        passwordLabel = Label(self.gui, text = "Password", bg = "lightgrey").pack()
        self.passField = Entry(self.gui)
        self.passField.pack()
        
        result = Button(self.gui,text = "Result",fg = "Black",
                        bg = "gray", command = self.password).pack()

        clear = Button(self.gui,text = "Clear All",fg = "Black",
                        bg = "Red", command = self.clearAll).pack()
        self.gui.mainloop()

    def password(self):
        self.clearAll()
        String = random.sample(string.ascii_letters, 6) + random.sample(string.digits, 4)
        random.SystemRandom().shuffle(String)
        password=''.join(String)
        self.passField.insert(10, str(password))

    def clearAll(self) :
        self.passField.delete(0, END)

def main():
    app = PasswordGenetorGUI()

if __name__ == "__main__" :
    main()
# Slip6_2B
from tkinter import Label, Tk

def main():
    top=Tk()
    top.title="font style"
    label=Label(top,text="this is text with style",font=("Helvetica",25))
    label.pack()
    top.mainloop()

if __name__=="__main__":
    main()
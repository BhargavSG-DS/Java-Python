import tkinter as tk
import datetime
import dateutil.parser as dparser

class Application:
    def getAge(self):
        born = dparser.parse(self.Birthday.get(),fuzzy=True)
        today = datetime.date.today()
        self.Result = tk.Label(self.win,text=str(today.year - born.year - ((today.month, today.day) < (born.month, born.day)))).pack()
        return
    
    def __init__(self):
        self.win = tk.Tk()
        self.win.geometry('400x200')
        self.win.title('Slip1_2B')

        logwin = tk.LabelFrame(
            self.win,
            text='Enter Details',
            padx=10,
            pady=10
        )
        logwin.pack()

        tk.Label(
            logwin, 
            text='Birthday : ',
            pady=10
        ).grid(row=0, column=0)

        self.Birthday = tk.Entry(logwin, width=20)
        self.Birthday.grid(row=0, column=1)
        
        tk.Button(self.win, text="Calculate", width=30, command=self.getAge).pack()
        tk.Button(self.win, text="Exit", width=30, command=self.close).pack()
        self.win.mainloop()
    
    def close(self):
        self.win.destroy()

def main():
    Application()
    return


if __name__ == "__main__":
    main()
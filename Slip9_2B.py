# Slip9_2B
from tkinter import*

class Application:
    def __init__(self):
        self.root=Tk()
        self.root.title('Prime, Perfect or Armstrong number')
        self.root.geometry('300x200')
        self.numberField=Entry(self.root)
        self.numberField.pack()

        Button1=Button(self.root,text='Button',command=lambda:[self.armstrong(),self.prime(),self.perfect()])
        Button1.pack()

        self.prime2=IntVar()
        self.perfect2=IntVar()
        self.armstrong2=IntVar()

        self.armstrong1=Radiobutton(self.root,text='armstrong',variable=self.armstrong2,value=1)
        self.prime1=Radiobutton(self.root,text='prime',variable=self.prime2,value=1)
        self.perfect1=Radiobutton(self.root,text='perfect',variable=self.perfect2,value=1)
        self.armstrong1.pack()
        self.prime1.pack()
        self.perfect1.pack()

        self.root.mainloop()


    def perfect(self):
        number=int(self.numberField.get())
        count = 0
        for i in range(1, number):
            if number % i == 0:
                count = count + i
        if count == number:
            self.perfect1.select()
            print(number, 'The number is a Perfect number!')
        else:
            self.perfect1.deselect()
            print(number, 'The number is not a Perfect number!')

    def armstrong(self):
        number=int(self.numberField.get())
        count = 0
        temp = number
        while temp > 0:
            digit = temp % 10
            count += digit ** 3
            temp //= 10 
        if number == count:
            self.armstrong1.select()
            print(number, 'is an Armstrong number')
        else:
            self.armstrong1.deselect()
            print(number, 'is not an Armstrong number')

    def prime(self):
        number=int(self.numberField.get())
        if number > 1:
            for i in range(2,number):
                if (number % i) == 0:
                    self.prime1.deselect()
                    print(number,"is not a prime number")
                    print(i,"times",number//i,"is",number)
                    break
                else:
                    self.prime1.select()
                    print(number,"is a prime number")
        else:
            self.prime1.deselect()
            print(number,"is not a prime number")

def main():
    app = Application()

if __name__=="__main__":
    main()
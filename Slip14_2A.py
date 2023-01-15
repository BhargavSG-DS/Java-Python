# Slip14_2A
from tkinter import *
from math import pi
from tkinter import messagebox

def clearAll() :
    RadiusField.delete(0, END)
    HeightField.delete(0, END)
    volumeField.delete(0, END)
    areaField.delete(0,END)
 
def checkError() : 
    if (RadiusField.get() == "" or HeightField.get() == "") :
        messagebox.showerror("Input Error")
        clearAll()
        return -1

def result() :
    value = checkError()
    if value == -1 :
        return 
    else :
        Radius = int(RadiusField.get())
        Height = int(HeightField.get())
        
        volume=round(pi*Height*Radius**2,2)
        area=round((2*pi*Radius*Height)+(2*pi*Radius**2),2)
        
        volumeField.insert(10, str(volume))
        areaField.insert(10, str(area))
  
if __name__ == "__main__" :
    gui = Tk()
    gui.configure(background = "light green")
    gui.title("cylinder surface area and volume of cylinder")
    gui.geometry("300x175")
 
 
 
    radius = Label(gui, text = " give radius", bg = "#00ffff") 
    height = Label(gui, text = "give height", bg = "#00ffff") 
    area = Label(gui, text = "Area", bg = "#00ffff")
    volume = Label(gui, text = "Volume", bg = "#00ffff")
    
    resultlabel = Label(gui, text = "RESULT", bg = "#00ffff")
    
    resultbutton = Button(gui, text = "Result", fg = "Black",
                        bg = "gray", command = result)
    clearAllEntry = Button(gui, text = "Clear All", fg = "Black",
                        bg = "Red", command = clearAll) 

    RadiusField = Entry(gui)
    HeightField = Entry(gui)
    volumeField = Entry(gui)
    areaField =Entry(gui)

    radius.grid(row = 0, column = 0)
    height.grid(row = 0, column = 2)
    area.grid(row = 2, column = 0)
    volume.grid(row = 2, column = 2)

    resultlabel.grid(row = 4, column = 1)
    resultbutton.grid(row = 5, column = 1)
        
    RadiusField.grid(row = 1, column = 0)
    HeightField.grid(row = 1, column = 2)

    areaField.grid(row=3,column=0)
    volumeField.grid(row = 3, column = 2)
    clearAllEntry.grid(row = 6, column = 1)

    gui.mainloop()
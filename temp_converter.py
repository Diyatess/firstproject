from tkinter import *

master = Tk()
master.title("Temperature Converter")
master.geometry('400x200')
Label(master, text="Temperature in F").grid(row=0, sticky=W)
Label(master, text="Result:").grid(row=3, sticky=W)

mainloop()
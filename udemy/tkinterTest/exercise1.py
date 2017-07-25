from tkinter import *
window = Tk()

def convert():
    ori = float(e1_value.get())
    t1.insert(END,ori*1000)
    t2.insert(END,ori*2.20462)
    t3.insert(END,ori*35.274)

b1 = Button(window,text='Converter',command=convert)
b1.grid(row=0,column=0)

e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1 = Text(window,heigh=1,width=30)
t1.grid(row=1,column=0)

t2 = Text(window,heigh=1,width=30)
t2.grid(row=1,column=1)

t3 = Text(window,heigh=1,width=30)
t3.grid(row=1,column=2)

window.mainloop()

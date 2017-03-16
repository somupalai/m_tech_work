import Tkinter as t
so = t.Tk()
so.title("sonali")
str1 = t.StringVar(so)

def adn():
    butn.configure(text = "iter"+str1.get())
    butn.grid(column=1, row=1)

name = t.Label(so,text="sonali")
butn = t.Button(so,text="sonali",command = adn)


txt = t.Entry(so,textvariable = str1)

txt.grid(row = 0,column=4)
butn.grid(row = 0,column=2)
name.grid(row = 0,column=0)

so.mainloop()

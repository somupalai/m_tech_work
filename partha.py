import Tkinter as t
ab = t.Tk()
ab.title("partha")
str1 = t.StringVar(ab)

def adn():
    butn.configure(text = "rout"+str1.get())
    butn.grid(column=1, row=1)

name = t.Label(ab,text="partha")
butn = t.Button(ab,text="partha",command = adn)


txt = t.Entry(ab,textvariable = str1)

txt.grid(row = 0,column=4)
butn.grid(row = 0,column=2)
name.grid(row = 0,column=0)

ab.mainloop()

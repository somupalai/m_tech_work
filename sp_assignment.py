import Tkinter as t
sd = t.Tk()
sd.title("sashank")
str1 = t.StringVar(sd)




def adn():
    print "sashank"
    butn.configure(text = "assignment"+str1.get())
    butn.grid(column=1, row=1)

name = t.Label(sd,text="sashank")
butn = t.Button(sd,text="sashank",command = adn)


txt = t.Entry(sd,textvariable = str1)



txt.grid(row = 0,column=4)
butn.grid(row = 0,column=2)
name.grid(row = 0,column=0)






sd.mainloop()

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 10:58:22 2017

@author: student
"""

import Tkinter as t

def v_r_c():
    sg = float(s_g.get())
    wc = float(w_c.get())
    ds = float(d_s.get())
    print wc*sg/ds


v_r = t.Tk()
a = "void ratio calculator"
v_r.title(a)
v_r.minsize(500,500)



s_g_ = t.Label(v_r, text = "Enter specific gravity")
s_g_.grid(column =0, row = 0)
s_g = t.StringVar(v_r)
s_g_ent  = t.Entry(v_r,textvariable= s_g)
s_g_ent.grid(column=1, row= 0)


w_c_ = t.Label(v_r, text = "Enter water content(%)")
w_c_.grid(column =0, row = 1)

w_c = t.StringVar(v_r)
w_c_ent  = t.Entry(v_r,textvariable= w_c)
w_c_ent.grid(column=1, row= 1)



d_s_ = t.Label(v_r, text = "Enter degree of saturation(%)")
d_s_.grid(column =0, row = 2)

d_s = t.StringVar(v_r)
d_s_ent  = t.Entry(v_r,textvariable= d_s)
d_s_ent.grid(column=1, row=2)


v_r_calc = t.Button(v_r,text = "find void Ratio", command = v_r_c)


v_r_calc.grid(column=1, row =3)

v_r.mainloop()

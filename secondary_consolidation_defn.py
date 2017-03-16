import math as m
def sc(Cs,Ho,eo,t1,t2):
    return float((Cs*Ho*(m.log((t2/t1),10)))/(1+eo))
print sc(12.0,45.0,6.0,12.0,4.0)

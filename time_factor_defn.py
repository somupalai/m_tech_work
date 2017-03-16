import math as m
#def tf(pi,u):
    #return(3.141*u*u)/4
#print tf(3.141,45)
import math as m
def tv(u):
    if u <= .6:
        return (m.pi*u*u)/4
    else:
        return (-0.9332)* m.log(1-u,10) - 0.0851
print tv(.7)


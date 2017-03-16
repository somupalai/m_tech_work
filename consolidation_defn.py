import math as m
def cs(Cc,Ho,eo,sig1,sig2):
    return (Cc*Ho*(m.log((sig2/sig1),10)))/(1+eo)
print cs(11,23,45,2,9)

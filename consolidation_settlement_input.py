import math
print "the value of Cc"
Cc = float(input())
print "the value of Ho"
Ho = float(input())
print "the value of eo"
eo = float(input())
print "the value of sig1"
sig1 = float(input())
print "the value of sig2"
sig2 = float(input())
#import math
print "the value of delH"
delH = (Cc*Ho*(math.log((sig2/sig1),10)))/(1+eo)
print delH

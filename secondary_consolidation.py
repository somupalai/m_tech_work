import math
print "the value of Cs"
Cs = float(input())
print "the value of Ho"
Ho = float(input())
print "the value of eo"
eo = float(input())
print "the value of t1"
t1 = float(input())
print "the value of t2"
t2 = float(input())
#print "the value of Ss"
Ss = (Cs*Ho*(math.log((t2/t1),10)))/(1+eo)
print Ss
      

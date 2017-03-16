import math as m
#print "the value of Pi"
#Pi = float(input())
print "the value of u"
u = float(input())
print "the value of Tv"
#Tv = float(input())
#Tv = (m.pi*u*u)/4
#print Tv
Tv = (-0.9332)* m.log(1-u,10) - 0.0851
print Tv

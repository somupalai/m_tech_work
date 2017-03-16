print "input value of A"
A = float(input())
print "input pore water pressure of B"
B = float(input())
print "input major principal stress of del_1"
del_1 = float(input())
print "input minor principal stress of del_3"
del_3 = float(input())
print "the value of del_u"
del_u = (B*del_3) + (A*(del_1 -del_3))
print del_u

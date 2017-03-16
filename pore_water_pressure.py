print "input value of A"
A = float(input())
print "input pore water pressure of B"
B = float(input())
#print "input major principal stress of del_1"
#del_1 = float(input())
#print "input minor principal stress of del_3"
#del_3 = float(input())
#del_u = (B*del_3) + (A*(del_1 -del_3))
#print "Value of del_u", del_u
print "input value of del_1final"
del_1final = float(input())
print "input value of del_1initial"
del_1initial = float(input())
#print del_1 (del_1final - del_1initial)
print "del_1"  
del_1 = (del_1final - del_1initial)
print "input value of del_3final"
del_3final = float(input())
print "input value of del_3initial"
del_3initial = float(input())
print "del_3" 
del_3 = (del_3final - del_3initial)
print "del_u" 
del_u = (B*del_3) + (A*(del_1 -del_3))
print del_u

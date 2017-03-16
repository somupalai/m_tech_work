import math
print "the value of posion's ratio"
mu = float(input())
print "the value of young's modouls"
E = float(input())
print "the value of constant pressure"
q = float(input())
print "the value of influense factor"
Ip = float(input())
print "the value of area"
a = float(input())
print "the value of immidiate settlement"
#Si = float(input())
Si = ((1-mu*mu)*(q*math.sqrt(a)*(Ip)))/(E)
print Si

# -*- coding: utf-8 -*-
from math import *
# (1.) * (2) = (2.) - float * int = float
# (1.) * (2.)= (2.) - float * float = float
# Python 2.x
# x = 1. * input("Lietotāj, lūdzu, ievadi argumentu (x): ")
# Python 2.x
# x = float(raw_input("Lietotāj, lūdzu, ievadi argumentu (x): "))
# Python 3.x
x = float(input("Lietotāj, lūdzu, ievadi argumentu (x): "))
y = sin(x)
print("sin(%.2f) = %.2f"%(x,y))
a0 = (-1)**0*x**1/(1)
S0 = a0
print("a0 = %.2f S0 = %.2f"%(a0,S0))
a1 = (-1)**1*x**3/(1*2*3)
S1 = a0 + a1
print("a1 = %.2f S1 = %.2f"%(a1,S1))
a2 = (-1)**2*x**5/(1*2*3*4*5)
S2 = a0 + a1 + a2
print("a2 = %.2f S2 = %.2f"%(a2,S2))
a3 = (-1)**3*x**7/(1*2*3*4*5*6*7)
S3 = a0 + a1 + a2 + a3
print("a3 = %.2f S3 = %.2f"%(a3,S3))

# -*- coding: utf-8 -*-
from math import sin
# S0, S1, S2, S3 -> S
x = float(input("Lietotāj, lūdzu, ievadi argumentu (x): "))
y = sin(x)
print("sin(%.2f) = %.2f"%(x,y))
a0 = (-1)**0*x**1/(1)
S = a0
print("a0 = %.2f S0 = %.2f"%(a0,S))
a1 = (-1)**1*x**3/(1*2*3)
#S1 = (a0) + a1
#S1 = S0 + a1
S = S + a1
print("a1 = %.2f S1 = %.2f"%(a1,S))
a2 = (-1)**2*x**5/(1*2*3*4*5)
#S2 = (a0 + a1) + a2
#S2 = S1 + a2
S = S + a2
print("a2 = %.2f S2 = %.2f"%(a2,S))
a3 = (-1)**3*x**7/(1*2*3*4*5*6*7)
#S3 = (a0 + a1 + a2) + a3
#S3 = S2 + a3
S = S + a3
print("a3 = %.2f S3 = %.2f"%(a3,S))

# -*- coding: utf-8 -*-
from math import sin as standarta_sinuss
# a0, a1, a2, a3 -> a
x = float(input("Lietotāj, lūdzu, ievadi argumentu (x): "))
y = standarta_sinuss(x)
print("sin(%.2f) = %6.2f"%(x,y))
#a0 = (-1)**0*x**1/(1)
a = (-1)**0*x**1/(1)
#S = a0
S = a
print("a0 = %6.2f S0 = %6.2f"%(a,S))
#a1 = (-1)**1*x**3/(1*2*3)
#a1 = a0 * (-1)*x*x/(2*3)
a = a * (-1)*x*x/(2*3)
#S = S + a1
S = S + a
print("a1 = %6.2f S1 = %6.2f"%(a,S))
#a2 = (-1)**2*x**5/(1*2*3*4*5)
#a2 = a1 * (-1)*x*x/(4*5)
a = a * (-1)*x*x/(4*5)
#S = S + a2
S = S + a
print("a2 = %6.2f S2 = %6.2f"%(a,S))
#a3 = (-1)**3*x**7/(1*2*3*4*5*6*7)
#a3 = a2 * (-1)*x*x/(6*7)
a = a * (-1)*x*x/(6*7)
#S = S + a3
S = S + a
print("a3 = %6.2f S3 = %6.2f"%(a,S))

# -*- coding: utf-8 -*-
import math
x = float(input("Lietotāj, lūdzu, ievadi argumentu (x): "))
y = math.sin(x)
print("sin(%.2f) = %6.2f"%(x,y))
k = 0
a = (-1)**0*x**1/(1)
S = a
print("a0 = %6.2f S0 = %6.2f"%(a,S))
k = 1
#a = a * (-1)*x*x/(2*3)
a = a * (-1)*x*x/((2*k)*(2*k+1))
S = S + a
#print("a1 = %6.2f S1 = %6.2f"%(a,S))
print("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))
k = 2
#a = a * (-1)*x*x/(4*5)
a = a * (-1)*x*x/((2*k)*(2*k+1))
S = S + a
#print("a2 = %6.2f S2 = %6.2f"%(a,S))
print("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))
k = 3
#a = a * (-1)*x*x/(6*7)
a = a * (-1)*x*x/((2*k)*(2*k+1))
S = S + a
#print("a3 = %6.2f S3 = %6.2f"%(a,S))
print("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))

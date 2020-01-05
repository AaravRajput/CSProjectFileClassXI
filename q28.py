import math
a = int(input("Enter coefficients a for quadratic equation ax^2+bx+c"))
b = int(input("Enter coefficients b for quadratic equation ax^2+bx+c"))
c = int(input("Enter coefficients c for quadratic equation ax^2+bx+c"))
d=(b*b)-(4*a*c)
xp = ((0-b)+math.sqrt(d))/(2*a)
xn = ((0-b)-math.sqrt(d))/(2*a)
print("The two roots for the given quadratic equation are {0} and {1}".format(xp,xn))
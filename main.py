import math
eps = 0.001

x = float(input('x='))
a = 1 # x ustu
fact = 1
p = 0
while True:
    fact = fact*a
    z = (x**a)/fact
    p =p+(-1)*z
    a = a + 1
    if math.fabs(z) < eps:
        break


print(p)

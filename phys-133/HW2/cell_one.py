print("Hello World!\n")
import numpy as np

x = 5
x = x**3 - 25

print(x)

y = np.linspace(0, 10, 11)
print("y[0] = " + str(y[0]) + "\ny[1] = " + str(y[1]) + "\ny[-1] = " + str(y[-1]))
print("y[1:5] = ")
print(y[1:5])
print("y[5:] = ")
print(y[5:])

mask = (y>3)

print("mask = ")
print(mask)
print("y[mask] = ")
print(y[mask])
print("y[y>3] = ")
print(y[y>3])

a = np.array([0,1,2,3])
b = np.array([0, 15, 30, 45])

print("2*a+a*b = ")
print(2*a+a*b)

x = 14.35244
print("%d"%(x))
print("%.3f"%(x))
print("%.4e"%(x))
print("%05d"%(x))

def myfunc1(x):
    return x**2

print("myfunc1(2.7) = ")
print(myfunc1(2.7))

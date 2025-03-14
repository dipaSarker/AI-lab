#y1 = g1(f1(x)) where f1(x) = w1x + b1, u1 = f1(x), and g1(u1) = 1/ (1 + e^(-u1))
           #y2 = g2(f2(x)) where f2(x) = w2x + b2, u2 = f2(x), and g2(u2) = 1/ (1 + e^(-u2))
           #y = g3(f3(v)) where f3(v) = w3y1 + w4y2 + b, w = f3(v), and g3(w) = 1/ (1 + e^(-w))



import numpy as np
import matplotlib.pyplot as plt


def f1(x, w1, b1):
    return w1 * x + b1

def g1(u1):
    return 1 / (1 + np.exp(-u1))

def f2(x, w2, b2):
    return w2 * x + b2

def g2(u2):
    return 1 / (1 + np.exp(-u2))

def f3(v, w3, w4, b):
    return w3 * v[0] + w4 * v[1] + b

def g3(w):
    return 1 / (1 + np.exp(-w))



w1 = 0.5  
b1 = 1
w2 = -0.8 
b2 = -2
w3 = 0.7 
w4 = 0.3 
b = 0


x = np.arange(-10, 10.1, 0.1)


y1 = g1(f1(x, w1, b1))
y2 = g2(f2(x, w2, b2))


v = np.array([y1,y2])


y = g3(f3(v, w3, w4, b))



plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='y1')
plt.plot(x, y2, label='y2')
plt.plot(x, y, label='y')
plt.xlabel('x')
plt.ylabel('y')
plt.title('y1, y2 and y as functions of x')
plt.legend()
plt.grid(True)
plt.show()


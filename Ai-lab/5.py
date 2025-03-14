import numpy as np
import matplotlib.pyplot as plt

x_values = np.arange(-10,10,0.1)
y_values = np.arange(-10,10,0.1)



#y = g(f(x)) where u = f(x) = wx + b and y = g(u) = 1/ (1 + e^(-u))

def f(x, w, b):
   return w * x + b


def g(u):
  return 1 / (1 + np.exp(-u))
w = 2.0  
b = -1.0  
y_values = []
for x in x_values:
  u = f(x, w, b)
  y = g(u)
  y_values.append(y)

  print("x\ty")
for x, y in zip(x_values, y_values):
  print("{:.2f}\t{:.4f}".format(x, y))
plt.plot(x_values, y_values)
plt.title("y = g(f(x))")
plt.grid(True)
plt.show()





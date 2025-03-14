import numpy as np
import matplotlib.pyplot as plt

x_values = np.arange(-10,10,0.1)
y_values = np.arange(-10,10,0.1)
print(x_values)



#y = wx + b
def func_1(w,x,b):
    return w*x+b
w=1
b=2
Function_1=func_1(w,x_values,b)
plt.subplot(3,3,1)
plt.plot(x_values,Function_1,label="Linear function")
plt.title("Linear function")
plt.legend()
plt.grid()
plt.tight_layout()
#plt.show()



#y = x^2
def func_1(x):
    return (x**2)
Function_1=func_1(x_values)
plt.subplot(3,3,2)
plt.plot(x_values,Function_1,label="Non_linear function")
plt.title("Non_linear function")
plt.legend()
plt.grid()
plt.tight_layout()
#plt.show()



#y = 1/ (1 + e^(-x))
def sigmoid(x):
    return 1 / (1 + np.pow(np.e,-x))
x = 0.5  
sigmoid_1=sigmoid(x_values)
plt.subplot(3,3,3)
plt.plot(x_values,sigmoid_1,label="Sigmoid function")
plt.title("Sigmoid function")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()



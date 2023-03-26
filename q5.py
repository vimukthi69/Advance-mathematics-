import matplotlib.pyplot as plt
import numpy as np
import sympy as sym


# --------------- Part a ---------------
x_coordination = np.linspace(-10, 10, 100)
y_coordination = 1/(1+np.exp(-x_coordination))

plt.plot(x_coordination, y_coordination)
plt.ylabel("f(x)")
plt.xlabel("x")
plt.show()

# --------------- Part b ---------------
x_coordination = np.linspace(-10, 10, 100)
y_coordination = 1/(1+np.exp(-x_coordination))
df = np.exp(-x_coordination)/(1 + np.exp(-x_coordination) ** 2)
plt.plot(x_coordination,df)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

# --------------- Part c ---------------

# a)
x_coordination = np.arange(-2*np.pi, 2*np.pi, 0.1)
y_coordination = np.sin(np.sin(2*x_coordination))
plt.plot(x_coordination, y_coordination)
plt.show()

# b)
x_coordination = np.linspace(-10, 10, 100)
y_coordination = -x_coordination**3-2*x_coordination**2+3*x_coordination+10
plt.plot(x_coordination,y_coordination)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

# c)

x_coordination = np.linspace(-10, 10, 100)
y_coordination = np.exp(-0.8*x_coordination)
plt.plot(x_coordination,y_coordination)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# d)
x_coordination = np.arange(-2*np.pi, 2*np.pi, 0.1)
y_coordination = x_coordination**2 * np.cos(np.cos(2*x_coordination))- 2 * np.sin(np.sin(x_coordination-(np.pi/3)))
plt.plot(x_coordination,y_coordination)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

# e)
def g(x):
    if -np.pi <= x < 0:
        return 2 * np.cos(x + np.pi / 6)
    if 0 <= x < np.pi:
        return x * np.exp(-0.4 * x ** 2)
    if x <= -np.pi:
        m = x + (2 * np.pi)
        result = g(m)
        return result
    if x > np.pi:
        m = x - (2 * np.pi)
        result = g(m)
        return result


x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = [g(l) for l in x]
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('g(x)')
plt.show()


# --------------- Part d ---------------

# a)
def logistic_function(x):
    return 1 / (1 + np.exp(-x))

def f(x):
    return np.sin(np.sin(2 * x))


x = np.linspace(-10, 10, 100)
y = logistic_function(f(x))
plt.plot(x,y)
plt.show()

# b)
def f(x):
    return -x ** 3 - 2 * x ** 2 + 3 * x + 10


x = np.linspace(-10, 10, 100)
y = logistic_function(f(x))
plt.plot(x,y)
plt.show()

# c)
def f(x):
    return np.exp(-0.8 * x)


x = np.linspace(-10, 10, 100)
y = logistic_function(f(x))
plt.plot(x, y)
plt.show()

# d)
def f(x):
    return x ** 2 * np.cos(np.cos(2 * x)) - 2 * np.sin(np.sin(x - np.pi / 3))


x = np.linspace(-10, 10, 100)
y = logistic_function(f(x))

plt.plot(x, y)
plt.show()

# e)

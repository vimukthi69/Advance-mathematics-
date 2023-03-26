import math
import matplotlib.pyplot as plt
import numpy as np
import sympy

# --------------- Part a ---------------
x = np.linspace(-5 * np.pi, 7 * np.pi)
y = x * np.cos(x / 2)
plt.ylabel("f(x)")
plt.xlabel("x")
plt.title("function")
plt.plot(x, y)
plt.show()

# --------------- Part b ---------------
def cosineTaylorSeries(x, rangeValues):
    x = x % (2 * np.pi)
    total = 0
    for i in range(0, rangeValues + 1):
        total += ((-1) ** i) * (x ** (2 * i) / math.factorial(2 * i))
    return total

x = np.pi / 2
n = 10
print(cosineTaylorSeries(x, n))

# --------------- Part c ---------------
def function(x):
    return sympy.cos(x)

x = sympy.Symbol('x')
x0 = np.pi / 2
count = 60

Series = sympy.series(function(x), x0, count)
rangeOfFunction = np.linspace(-10, 10, 100)
y = [Series.evalf(subs={x: xValues}) for xValues in rangeOfFunction]

plt.title("Taylor Series")
plt.plot(rangeOfFunction, y)
plt.show()

# --------------- Part d ---------------
def func_cos(x, n):
    cos_approx = 0
    for i in range(n):
        coef = (-1) ** i
        num = x ** (2 * i)
        denom = math.factorial(2 * i)
        cos_approx += (coef) * ((num) / (denom))

    return cos_approx


angle_rad = (math.radians(30))
coefficent_value = math.radians(60)
out = coefficent_value * func_cos(angle_rad, 5)
print(out)

angles = np.arange(-2*np.pi,2*np.pi,0.1)
p_cos = np.cos(angles)
t_cos = [func_cos(angle,3) for angle in angles]

fig, ax = plt.subplots()
ax.plot(angles,p_cos)
ax.plot(angles,t_cos)
ax.set_ylim([-5,5])
ax.legend(['cos() function','Taylor Series - 3 terms'])

plt.show()

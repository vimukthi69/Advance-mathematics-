import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
import math

# --------------- Part a ---------------
x_range = np.linspace(-4 * np.pi, 4 * np.pi, 1000)
periodValue = 2 * np.pi + x_range


def f(x):
    global result
    if 0 > x >= -np.pi:
        return (x ** 2) + 1
    if 0 <= x <= np.pi:
        return x * np.exp(-x)
    if x < -np.pi:
        p = x + (2 * np.pi)
        result = f(p)
    if x > np.pi:
        p = x - (2 * np.pi)
        result = f(p)

    return result


y_values = [f(l) for l in x_range]
plt.plot(periodValue, y_values)
plt.show()

# --------------- Part b and Part c ---------------
x = sym.symbols('x')
n = sym.symbols('n', integer=True, positive=True)

ms = np.empty(150, dtype=object)
xrange = np.linspace(4 * np.pi, -4 * np.pi, 1000)
y = np.zeros([151, 1000])

eq = (x ** 2) + 1
eq2 = x*sym.exp(-1*x)

a0 = (1 / (sym.pi)) * (eq.integrate((x, -1*sym.pi, 0)) + eq2.integrate((x, 0, sym.pi)))
print(a0)

an = (1 / sym.pi) * (sym.integrate((eq * sym.cos(n * x)), (x, -1*sym.pi, 0)) + sym.integrate((eq2 * sym.cos(n * x)), (x, 0, sym.pi)))
print(an)

bn = (1 / sym.pi) * (sym.integrate((eq * sym.sin(n * x)), (x, -1*sym.pi, 0)) + sym.integrate((eq2 * sym.sin(n * x)), (x, 0, sym.pi)))
print(bn)

ms[0] = a0/2

f = sym.lambdify(x, ms[0], 'numpy')
y[0, :] = f(xrange)

for m in range(1, 150):
    ms[m] = ms[m - 1] + an.subs(n, m) * sym.cos(m * x) + bn.subs(n, m) * sym.sin(m * x)
    f = sym.lambdify(x, ms[m], 'numpy')
    y[m, :] = f(xrange)

plt.plot(xrange, y[1, :])
plt.plot(xrange, y[4, :])
plt.plot(xrange, y[149, :])

plt.legend(["1", "5", "150"])
plt.show()

# --------------- Part d ---------------
actual = [y[1, :]]
predicted = [y_values]

MSE = np.square(np.subtract(actual, predicted)).mean()

rsme = math.sqrt(MSE)
print("Root Mean Square Error for 1st harmonic is :")
print(rsme)

actual = [y[4, :]]

MSE = np.square(np.subtract(actual, predicted)).mean()

rsme = math.sqrt(MSE)
print("Root Mean Square Error for 5th harmonic is :")
print(rsme)

actual = [y[149, :]]

MSE = np.square(np.subtract(actual, predicted)).mean()

rsme = math.sqrt(MSE)
print("Root Mean Square Error for 150th harmonic is :")
print(rsme)

import math

def f(x):
    return x*4 - 7*x*2 + x - 8

def bisseccao(f, a, b, tol):
    it = 0
    while abs(b-a) > tol:
        it += 1
        m = (a+b)/2
        if f(m)*f(a) < 0:
            b = m
        else:
            a = m
    return (a+b)/2, it

a, b = -5, 5
tol = 1e-6

x_bissec, it_bissec = bisseccao(f, a, b, tol)
print("Valor aproximado da raiz pelo método da bissecção:", x_bissec)
print("Número de iterações da bissecção:", it_bissec)

from scipy.optimize import newton

def f(x):
    return x*4 - 7*x*2 + x - 8

x0 = 0.5
x_quasi_newton = newton(f, x0, tol=1e-6)
print("Valor aproximado da raiz pelo método Quasi-Newton:", x_quasi_newton)
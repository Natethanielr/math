import numpy as np

# functions defined as python functions

# Polynomials


def linear(x, a, b):
    return a*x + b


def quadratic(x, a, b, c):
    return a*x**2 + b*x + c


def cubic(x, a, b, c, d):
    return a*x**3 + b*x**2 + c*x + d


def quartic(x, a, b, c, d, e):
    return a*x**4 + b*x**3 + c*x**2 + d*x + e


# Exponential


def exponential(x, a):
    return np.exp(a*x)


def general_exp(x, a):
    return np.power(x, a)


# trigonometric


def sine(a, x):
    return np.sin(a*x)


def cosine(a, x):
    return np.cos(a*x)

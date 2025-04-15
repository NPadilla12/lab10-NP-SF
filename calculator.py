# https://github.com/NPadilla12/lab10-NP-SF
# Partner 1: Nicholas Padilla
# Partner 2: Sayyed Faisal


"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.

"""


import math


# First example

def add(a, b): 
    return a + b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def exp(a, b):
    return math.pow(a, b)


def subtract(a, b):
    return a - b

def logarithm(a, b):
    if a <= 0:
        raise ValueError
    elif b <= 0:
        raise ValueError
    else:
        return math.log(b, a)


def square_root(a):
    if a > 0:
        return math.sqrt(a)
    else:
        raise ValueError()


def hypotenuse(a, b):
    return math.hypot(a, b)

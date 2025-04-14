"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
def add(a, b): 
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return total = a / b
    else:
        raise ZeroDivisionError()
def logarithm(a, b):
    if a != 0:
        return math.log(b, a)
    else:
        raise ValueError()
def exponent(a, b):
    return a ** b
def square_root(a):
    if a > 0:
        return math.sqrt(a)
    else:
        raise ValueError()
def hypotenuse(a, b):
    return math.hypot(a, b)
    

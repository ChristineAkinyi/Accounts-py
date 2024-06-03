def add(x,y):
    result = x+y
    return result

def subtract(a,b):
    result = a-b
    return result

def divide(c,d):
    """hello"""
    result = c/d
    return result

def multiply(e,f):
    result = e*f
    return result

def remainder(g,h):
    result = g%h
    return result

def powerof(i,j):
    result = i**j
    return result

def sum(*numbers):
    total = 0
    for number in numbers:
        total+=number
    return total

def multiply_many(*numbers):
    multiply=1
    for number in numbers:
        multiply*=number
    return multiply

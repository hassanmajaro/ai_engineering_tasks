# Math Operations

def add(a, b):
    return a + b

def sub(a, b):
    return a - b 

def mul(a, b):
    return a * b 

def div(a, b):
    if b == 0:
        return "Not possible. Denominator cannot be zero"
    else:
        return a / b
        
        
def exp(a, b):
     return a ** b

def sq_root(a):
     return a ** 0.5

def cube_root(a):
     return a ** 0.33333333

def mod(a, b):
    if b == 0:
        return "Not possible. Denominator cannot be zero\n"
    else:
        return a % b
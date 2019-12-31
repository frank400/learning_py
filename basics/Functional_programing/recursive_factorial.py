from functools import reduce


def  factorial(n):
    return n*(factorial(n-1) if (n-1)>1 else 1)

print(factorial(3))
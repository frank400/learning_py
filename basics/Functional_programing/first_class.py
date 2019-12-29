from math import sqrt

def half(x):
    return x/2

def square(x):
    return sqrt(x)

def main():
    #first class functions may be used as dates in python
    funcs=[half,square]*10
    for func,number in zip(funcs,range(1,21)):
        print(f'function name :{func.__name__} |number:{number}|result:{func(number)}')

if __name__=='__main__':
    main()
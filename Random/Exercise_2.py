def factorial(x):
    if x==0:
        return 1
    return x*factorial(x-1)

    
if __name__=='__main__':
    x=int(input())
    print(factorial(x))

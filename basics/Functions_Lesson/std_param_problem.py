def fib(sequence=[0,1]):
    sequence.append(sequence[-1]+sequence[-2])
    return sequence

if __name__=='__main__':
    #the values of fib never restart even when we change the variable
    result=fib()
    print(result,id(result))
    print(fib())
    restart=fib()
    print(restart,id(restart))
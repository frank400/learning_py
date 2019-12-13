def fib(sequence=None):
    #or operator uses the list since the sequence arg is False
    sequence=sequence or [0,1]
    sequence.append(sequence[-1]+sequence[-2])
    return sequence

if __name__=='__main__':
    #then every time we call the fib funcion,if we don't use any param,it will always be equal to [0,1]
    result=fib()
    print(result,id(result))
    print(fib())
    restart=fib()
    print(restart,id(restart))
def fibonacci(limite,resultado=(0,1)):      
    if len(resultado)==limite:
        return resultado
    else:
        return fibonacci(limite,resultado+(sum(resultado[-2:]),))

if __name__=='__main__':
    print("-------**calcule uma determinada quantidade de números de fibonacci**-------")
    fim=input("digite um número de números de fibonacci: ")
    for fib in fibonacci(int(fim)):
        print(fib,end="||")
    print("\n")
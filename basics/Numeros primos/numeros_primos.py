def calcula(limite):
    primos=[2]
    for i in range(3,limite+1):
        for j in primos:
            if i%j==0:
                break
        else:
            primos.append(i)
    return primos


def finalização():
    print("by frank")
    _ = input("aperte enter para finalizar")

if __name__=='__main__':
    limite=input("digite um limite para os números primos:")
    primoF=calcula(int(limite))
    for i in range(len(primoF)):
        print(primoF[i],end="||")
    finalização()

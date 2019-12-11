from random import randint

def sorteia_numero():
    return randint(1,6)
if __name__=='__main__':
    numero=sorteia_numero()

    for i in range(1,7):
        if i==numero:
            print(f"Acertou o valor,O valor foi {i}")
            continue
        else:
            print("Não acertou o número.")
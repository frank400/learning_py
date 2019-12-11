from random import randint
from Modulo_7 import finalizacao

secret_number=randint(0,9)
guess_number=-1

if __name__ =='__main__':
    while guess_number != secret_number:
        guess_number=int(input("digite um numero inteiro:"))

    print(f"O número secreto é {secret_number} PARABÉNS!!!!!")
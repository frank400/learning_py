with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print("nome:{}||idade:{}".format(*registro.strip().split(',')))

_=input()
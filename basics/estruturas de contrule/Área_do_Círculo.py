from math import pi
import sys

def circulo(r):
    return float(r)**2 * pi


def help():
    if len(sys.argv) < 2:
        return True
    else:
        return False


def finalizacao():
    _ = input("XX-------- aperte enter para fechar o programa --------XX")
    

if __name__=='__main__':
    if help():
        print("informe o valor do raio ao digitar o comando!!!!!")
        print("sintaxe:{} <raio> ".format(sys.argv[0][2:]))

        finalizacao()

    elif not sys.argv[1].isnumeric():
        print("informe o valor do raio em números ao digitar o comando!!!!!")
        print("O raio deve ser um valor numerico imbecil")

        finalizacao()

    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print(f"O valor da área do círculo é : {area}")

        finalizacao()

import csv

#csv.reader():lê o arquivo e separa em uma lista pelas virgulas, é delicioso!!!
def read():
    with  open('desafio-ibge.csv') as arquivo:
        dados=arquivo.read()
        for cidade in csv.reader(dados.splitlines()):
            print(f"{cidade[8]}:{cidade[3]}")

if __name__ =='__main__':
    read()
    _ =input()

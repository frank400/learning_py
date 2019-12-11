import sys
def finalizacao():
    x = input("XX-------- aperte enter para fechar o programa --------XX")

def calcula_resultado(nota):
    if  not  nota.isnumeric():
        print("a nota deve ser um numero entre 0-10")

    else:
        if nota>9 and nota<=10:
            print("nota A")
            finalizacao()
            
        elif nota>8:
            print("nota A-")
            finalizacao()
            
        elif nota>7:
            print("nota B")
            finalizacao()
            
        elif nota>6:
            print("nota B-")
            finalizacao()
            
        elif nota>5:
            print("nota C")
            finalizacao()
            
        elif nota>4:
            print("nota C-")
            finalizacao()
            
        elif nota>3:
            print("nota D")
            finalizacao()
            
        elif nota>2:
            print("nota D-")
            finalizacao()
            
        elif nota>1:
            print("nota E")
            finalizacao()
            
        elif nota>=0:
            print("nota E-, se fudeu parceiro")
            finalizacao()
            
        else:
            print("nota invalida")
            finalizacao()
        
if __name__ =='__main__':
    nota=input("digite a nota do aluno:")
    calcula_resultado(nota)

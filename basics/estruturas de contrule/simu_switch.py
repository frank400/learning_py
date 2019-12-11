def dias_semana(dia_modulado):
    dias={
        1:'segunda',
        2:'terça',
        3:'quarta',
        4:'quinta',
        5:'sexta',
        6:'sábado',
        0:'domingo',
    }
    return dias.get(dia_modulado,"**valor invalido**")


def dia_modulo(dia):
    return dia%7

def final_semana(dia):
    if dia%7==0 or dia%7==6:
        return 'é final de semana'
    else:
        return 'não é final de semana'

if __name__=='__main__':
    for i in range(1,32):
        print(f"é dia {i} o dia da semana é {dias_semana(dia_modulo(i))} e {final_semana(i)}")
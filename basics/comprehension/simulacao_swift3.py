def final_semana(dia):
    dias={
        (6,0):'final de semana',
        tuple(range(1,6)):'dia de semana',
    }
    #gerador entra no dicionario e ve se o dia esta dentro dos da semana,
    #se sim o gerador recebe o tipo de dia é por isso percorrer o dict dias por items e com numeros e tipos
    #dessa forma verificando se o dia informado esta dentro dos numeros representados pelo  dict dias
    generator=(tipo for numeros,tipo in dias.items() if dia in numeros )

    #agr retorna o tipo do dia informado pelo proprio generator
    return next(generator,"**dia invalido")
    #função next por ser um generator

def dia_modulo(dia):
    if dia<=31:
        return dia%7
    else:
        return 7

if __name__=='__main__':
    dia=input("digite um dia do mês: ")
    print(final_semana(dia_modulo(int(dia))))
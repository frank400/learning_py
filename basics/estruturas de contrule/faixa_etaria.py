def faixa_etaria(idade):
    if 0 <= idade <18:
        return 'menor de idade'
    elif idade in range (18,65):
        return 'adulto'
    elif idade in range (65,100):
        return 'idoso'
    elif idade >= 100:
        return 'centenário'
    else:
        return 'idade inválida'

if __name__ == '__main__':
    for idade in (18,16,15,24,65,101):
        print(f"você tem {idade} logo você é um {faixa_etaria(idade)}")
#percorrer dicionario
produto={'name':'fucktoy','preço':14.00,
         'importado':False ,'Estoque':30}

for chave in produto:
    print (chave)

for valor in produto.values():
    print(valor)

for chave , valor in produto.items():
    print(f"{chave} = {valor}")
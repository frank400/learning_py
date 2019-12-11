#generators VS list comprehension:generators geram a lista sob demanda 
#equanto os list comprehension gera a lista toda
#consumindo menos memória


generator=(i**2 for i in range(1,11)if i%2==0)


#print(next(generator))
#print(next(generator))
#print(next(generator))
#print(next(generator))
#ou você pode chamar pelo for,sem utilizar o next


for numero in generator:
    print(numero)
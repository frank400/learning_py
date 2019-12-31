from functools import reduce

persons = [
    {'name': 'joseph', 'age': 18},
    {'name': 'max', 'age': 20},
    {'name': 'frank', 'age': 22},
    {'name': 'alexia', 'age': 32}
]

def main():
    ages_sum= reduce(lambda ages,p:ages +p['age'],persons,0)
    print(ages_sum)

if __name__=='__main__':
    main()
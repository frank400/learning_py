persons=[
    {'name':'joseph','age':18},
    {'name':'max','age':16},
    {'name':'frank','age':15},
    {'name':'alexia','age':32}
]

def main():
    legal_age=filter(lambda p:p['age']>18,persons)
    print(list(legal_age))
    big_name=filter(lambda p:len(p['name'])>=5,persons)
    print(list(big_name))

if __name__=='__main__':
    main()
persons=[
    {'name':'joseph','age':18},
    {'name':'max','age':20},
    {'name':'frank','age':22},
    {'name':'alexia','age':32}
]

def main():
    func=map(lambda person: f'Name:{person["name"]}|Age:{person["age"]}',persons)
    print(list(func))
    

if __name__=='__main__':
    main()

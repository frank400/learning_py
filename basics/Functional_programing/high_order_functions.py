# high order function can recive another function by arg and may return other function
from first_class import half, square


def processing(title, list, funct):
    print(title)
    for i in list:
        print(i,'=>',funct(i) if callable(funct) else '')

def main():
    list=[1,2,3,4]
    processing('title',list,half)

if __name__=='__main__':
    main()
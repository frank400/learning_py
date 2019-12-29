from math import pow

values=(
    {'base':2,'power':3},
    {'base':4,'power':5},
    {'base':5,'power':4}
)
total=tuple(
    map(        #for value in values:
                    #pow(value['base'],value['power'])

        lambda value:pow(value['base'],value['power']),values #<=this last one is for map function
    )   
        #lambda function only build the method and recives the values that will be used
)

def main():
    print(total)

if __name__=='__main__':
    main()

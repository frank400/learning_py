from math import pow

values=(
    {'base':2,'power':3},
    {'base':4,'power':5},
    {'base':5,'power':4}
)
total=tuple(
    map(
        lambda value:pow(value['base'],value['power']),values
    )
)

def main():
    print(total)

if __name__=='__main__':
    main()

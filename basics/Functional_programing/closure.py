def multiply_by_x(x):
    def calc_with_y(y):
        return x*y
    return calc_with_y

def main():
    double=multiply_by_x(2)
    triple=multiply_by_x(3)
    double_of_4=double(4)
    triple_of_5=triple(5)
    print(f'the double of 4 is {double_of_4} and the tiple of 5 is {triple_of_5}')

if __name__=='__main__':
    main()
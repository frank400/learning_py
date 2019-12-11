#packing is when you transform a list of parameters in a tuple
def sum_n(*numbers):
    sum=0
    for num in (numbers):
        sum+=num
    return sum


if __name__=='__main__':
    print(sum_n(1,2,5,6))
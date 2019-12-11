#unpacking will transform a tuple parameter into a list of parameters
def sum_4(a,b,c,d):
    return a+b+c+d


if __name__=='__main__':
    test_tuple=(2,3,4,5)
    print(sum_4(*test_tuple))
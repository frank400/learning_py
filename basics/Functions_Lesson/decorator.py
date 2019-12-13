def log(function):
    def intro(*args,**kwargs):
        print(f"Name of function is: {function.__name__}")
        print(f"args : {args}")
        print(f"kwargs : {kwargs}")
        result=function(*args,**kwargs)
        print(f"result of function is: {result}")
    return intro
    


@log
def sum(a,b):
    return a + b


@log
def mult(a,b):
    return a*b


if __name__=='__main__':
    sum(5,b=2)
    mult(15,b=3)
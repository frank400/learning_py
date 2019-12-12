def all_params(*args,**kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__=="__main__":
    #the kwargs will be empty
    all_params(1,2,3,4)
    #args=(1,2,3[4,5,6]) ,kwargs={cool:True,explosive:False}
    all_params(1,2,3,[4,5,6],cool=True,explosive=False)

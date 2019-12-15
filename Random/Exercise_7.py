#Y,X
if __name__=='__main__':
    items=[x for x in input().split(',')]
    y,x=int(items[0]),int(items[1])
    array=[[i*j for i in range(x)] for j in range(y)]
    print(array)

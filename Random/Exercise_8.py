if __name__=='__main__':
    items=[x for x in input().split(',')]
    items.sort()
    print(''.join(items),end=',')
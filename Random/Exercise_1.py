if __name__=='__main__':
    sequence=[]
    for i in range(2000,3201):
        if i%7==0 and not i%5==0:
            sequence.append(str(i))

    print(','.join(sequence))  
        
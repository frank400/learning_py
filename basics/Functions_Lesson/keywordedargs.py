#**kwargs
def result_F1_packing(**podium):
    for position,pilot in podium.items():
        print(f"{position} -> {pilot}")


def result_F1_unpacking(first,second,third):
    return f'1){first}\n2){second}\n3){third}'


if __name__=='__main__':
    result_F1_packing(first = 'L.Hamilton',
              second = 'Verstappen',
              third = 'Vettel')

    #or

    podium={'second' : 'Verstappen',
            'first' : 'L.Hamilton',            
            'third' : 'Vettel'}
    print(result_F1_unpacking(**podium))
    
class SimpleClass:
    conter=0

    def __init__(self):
        self.cont()
    
    @classmethod
    def cont(cls):
        cls.conter+=1

if __name__=='__main__':
    list=[SimpleClass(),SimpleClass()]
    print(SimpleClass.conter)
class String:
    def __init__(self,string=None):
        self.string=string
    
    def getStr(self):
        self.string=input()
    
    def printstr(self):
        return self.string.upper()

        
if __name__=='__main__': 
    x=String()
    x.getStr()
    print(x.printstr())
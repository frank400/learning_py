#we will over fload the += operator to it add a new feature to our site
class Site:
    def __init__(self,name,desc,owner):
        self.name=name
        self.desc=desc
        self.owner=owner
        self.features=[]
    
    def __str__(self):
        return f'the name of this site is :{self.name} this is what it is :{self.desc} it owner is :{self.owner} and it features are :'
    
    #def __iadd__(self,feature):
        #self._add_feature(feature)

    def _add_feature(self,feature):
        self.features.append(Feature(feature))
    
    def searchfeature(self,name):
        return [feature for feature in self.features if feature.name=='name'][-1]

class Feature():
    def __init__(self,name,desc=None):
        self.name=name
        self.desc=desc
    
    def __str__(self):
        return f'the name of feature is {self.name} and it does this:{self.desc}'

    def add_description(self,text):
        self.desc=text
    
def main():
    waze=Site(name='Waze',desc='A app to smartfones based on GPS navegation to cars',owner='Google')
    waze.features.append(Feature('GPS'))
    waze.searchfeature('GPS').add_description('track a path to vehicles by a global sistem of satellites')
    print(waze)
    print(waze.searchfeature('GPS'))

if __name__=='__main__':
    main()
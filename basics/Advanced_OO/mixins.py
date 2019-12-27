class HtmlToStringMixin:
    def __str__(self):        
        html=super().__str__() \
            .replace("(","<strong>")\
            .replace(")","</strong>")

        return f'<span>{html}</span>'

class Person:
    def __init__(self,name):
        self.name=name
    
    def __str__(self):
        return self.name

class Animal:
    def __init__(self,name,pet=True):
        self.name=name
        self.pet=pet

    def __str__(self):
        return self.name + ' (pet)' if self.pet else ''

class HtmlPerson(HtmlToStringMixin,Person):
    pass

class HtmlAnimal(HtmlToStringMixin,Animal):
    pass

if __name__=='__main__':
    man=HtmlPerson('john')
    cat=HtmlAnimal('cat')
    print(man)
    print(cat)
    
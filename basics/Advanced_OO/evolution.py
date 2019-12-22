class Human:
    specie = 'homo sapiens'

    def __init__(self, name):
        self.name = name
        self._age=None
    
    def get_age(self):
        return self._age
    
    def set_age(self,age):
        if age<0:
            raise ValueError('Age must be a positive value')
        self._age=age

    def from_caves(self):
        self.specie = 'homo neanderthalesis'
        return self

    @staticmethod
    def species():
        adjetives = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapies')
        return ('Australopithecus',) + tuple(f'Homo {adj}' for adj in adjetives)

    @classmethod
    def is_evolved(cls):
        return cls.specie == cls.species()[-1]


class Neaderthal(Human):
    specie = Human.species()[-2]


class HomoSapiens(Human):
    specie = Human.species()[-1]


if __name__ == '__main__':
    joseph=HomoSapiens('Joseph')
    #joseph.set_age(40)
    #print(f'joseph age is {joseph.get_age()}')
    joseph.set_age(-40)
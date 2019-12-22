from abc import ABCMeta, abstractproperty


class Human(metaclass=ABCMeta):
    specie = 'homo sapiens'

    def __init__(self, name):
        self.name = name
        self._age = None

    @abstractproperty
    def inteligence(self):
        pass

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError('Age must be a positive value')
        self._age = age

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
    @property
    def inteligence(self):
        return False


class HomoSapiens(Human):
    specie = Human.species()[-1]

    @property
    def inteligence(self):
        return True


if __name__ == '__main__':
    joseph = HomoSapiens('Joseph')
    joseph.age = 40
    print(f'joseph age is {joseph.age()}')

class Human:
    specie = 'homo sapiens'

    def __init__(self, name):
        self.name = name

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
    gronk=Neaderthal('Gronk')
    print(f'Evolution by the class:{",".join(HomoSapiens.species())}')
    print(f'Evolution by the instance:{",".join(joseph.species())}')
    print(f'is Joseph evolved? {joseph.is_evolved()}')
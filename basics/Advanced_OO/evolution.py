class Human:
    specie = 'homo sapiens'

    def __init__(self, name):
        self.name = name

    def from_caves(self):
        self.specie = 'homo neanderthalesis'
        return self


if __name__ == '__main__':
    joseph = Human('joseph')
    gronk = Human('gronk').from_caves()

    print(f'human.specie:{Human.specie}')
    print(f'gronk.specie:{gronk.specie}')

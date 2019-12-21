from .person import Person


class Seller(Person):
    def __init__(self, name, age, payment):
        super().__init__(name, age)
        self.payment = payment

    def __str__(self):
        return f'Name:{self.name}\nAge:{self.age}\nPayment:{self.payment}'

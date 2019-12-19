from person import Person
class Seller(Person):
    def __init__(self,name,age,payment):
        super().__init__(name,age)
        self.payment=payment
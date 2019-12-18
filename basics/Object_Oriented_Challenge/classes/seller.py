from person import person
class seller(person):
    def __init__(self,name,age,payment):
        super().__init__(name,age)
        self.payment=payment
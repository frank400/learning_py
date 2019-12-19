from .person import Person

def get_date(purchase):
    return purchase.date
class Client(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.purchases=[]

    def __str__(self):
        return f'Name:{self.name},adult:' 'True' if super().isAdult() else 'False'
    
    def regist_purchase(self,purchase):
        self.purchases.append(purchase)
    
    def get_last_purchase(self):
        return None if not self.purchases else sorted(self.purchases,key=get_date)[-1].date

    def get_total_purchase(self):
        total=0
        for purchase in self.purchases:
            total += purchase.value
        
        return total
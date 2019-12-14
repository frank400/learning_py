class Product:
    def __init__(self,price):
        self.price=price
    
    def discont(self,percent=5):
        percentage=percent/100
        return self.price -self.price*percentage

p1=Product(200)
promotion=input("how much you want of discont? ")
print(p1.discont(int(promotion)))
print(p1.price)

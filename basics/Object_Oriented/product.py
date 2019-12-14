class Product:
    def __init__(self,price=None,name=None,shop_name=None):
        self.price=price
        self.name=name
        self.shop_name=shop_name
    
    def __str__(self):
        return f'name of product is :{self.name}\nhis price is :{self.price}\nthe shop that it come from is:{self.shop_name}'
    
    def discont(self,percent=5):
        percentage=percent/100
        return self.price -self.price*percentage


if __name__=='__main__':
    print("*******enter the product properties****")
    price=int(input("how much do it cost? "))
    name=str(input("what is it name? "))
    shop=str(input("what is the name that it comes? "))

    p1=Product(price,name,shop)

    #first ask
    answer_1=int(input("enter 1 if you want to see the what this product is or  if not :"))
    assert answer_1==1 or answer_1==0
    if answer_1:
        print(p1)


    #second ask
    answer_2=int(input("enter 1 to calculate a discont to this product or 0 if not :"))
    assert answer_2==1 or answer_2==0
    if answer_2:
        promotion=input("how much percente of discont do you want? ")
        print(p1.discont(int(promotion)))

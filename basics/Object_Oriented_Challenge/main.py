from classes import Seller,Client,Purchase
from datetime import datetime

def main():
    client=Client('max',44)
    seller=Seller('Frank',55,1024)
    purchase_1=Purchase(client,datetime.now(),512)
    purchase_2=Purchase(client,datetime(2019,4,9),256)
    client.regist_purchase(purchase_1)
    client.regist_purchase(purchase_2)
    print(client)
    print(seller)

    total_values=client.get_total_purchase()
    print(f'total value of purchases {total_values}$ in {len(client.purchases)} purchases')
    print(f"last purchase date: {client.get_last_purchase()}")

    
if __name__=='__main__':
    main()
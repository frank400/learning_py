def calc_final_price(price,calc_tax,*params):
    return price + price*calc_tax(*params)


def tax_x(imported):
    return 0.33 if imported else 0.13


def tax_explosive(explosive,mult_fator=1):
    return 0.11*mult_fator if explosive else 0


if __name__=='__main__':
    price_start=input("enter a price to product: ")
    final_price=calc_final_price(int(price_start),tax_x,True)
    final_price=calc_final_price(final_price,tax_explosive,True,1.5)
    print(final_price)

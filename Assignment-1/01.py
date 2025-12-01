def generatebill(item,price,quantity=1,discount=0,taxrate=0.05):
    subtotal = price*quantity
    afterDiscount = subtotal - ((subtotal)*discount)/100
    afterTax = afterDiscount + ((afterDiscount)*taxrate)/100
    print(f"Item: {item} , Quantity: {quantity} , Price: {price} , Discount {discount}% , Tax: {taxrate}% , Total Bill: {afterTax} \n")
    
generatebill("Mobile" , 20000) # for (i)
generatebill("TV" , 15000 , 5)
generatebill("Bike" , 90000 , discount=10 , taxrate=12)
generatebill("Car" , 1000000 , 2 , 15 , 20)

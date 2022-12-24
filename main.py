def enterProduct():
    buyingData = {}
    enterdetail = True
    while enterdetail:
        detail = input("Press P to add product and Q to add Quit: - ")
        detail.replace(" ", "")
        det = detail.upper()
        if det == 'P':
            product = input("Enter the product Name: -")
            quantity = int(input("Enter the quantity of the proiduct: - "))
            buyingData.update({product:quantity})
        elif det == 'Q':
            enterdetail = False
        else:
            print('Please select the correct option') 
        return buyingData
def getPrice(product, quanitity):
    priceData = {
        'Biscuit':10,
        'Cake':300,
        'chocolate': 40,
        'ice-cream' : 10,
        'Apple': 40
    }
    subtotal = priceData[product]*quanitity
    print(product +':$'+ str(priceData[product])+'x'+str(quanitity)+'='+str(subtotal))
    return subtotal
def getdiscount(billamount, memebership):
    discount = 0
    if billamount>=25:
        if memebership == 'Gold':
            billamount=billamount*0.80
            discount=20
        elif memebership == 'silver':
            billamount = billamount*0.90
            discount=10
        elif memebership == 'Bronze':
            billamount = billamount*0.95
            discount=5
        print(str(discount)+'% off for'+ memebership+ 'membership on total amount: $'+ str(billamount))
    else:
        print('No discount on the amount less then $25')
        return(billamount)
def makebill(buyingData, membership):
    billamount = 0
    for key, value in buyingData.items():
        billamount+= getPrice(key,value)
        billamount = getdiscount(billamount, membership)
        print('The discount amount is $'+ str(billamount))

    
buyingData = enterProduct()
membership = input('Enter the customer membership: - ')
makebill(buyingData,membership) 
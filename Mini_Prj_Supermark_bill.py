from datetime import datetime
name= input("Enter Your Name:")
#List of Items
list = '''
Rice    Rs 25/kg
Sugar   Rs 35/kg
Oil     Rs 90/Litre
Barley  Rs 50/kg
Wheat   Rs 30/kg
Apples  Rs 200/

'''

# print(List)
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

#Rate for Items
#Written in Dictionary format like Key-value pairs
items={'Rice':25,'Sugar':35, 'Oil':90, 'Barley':50, 'Wheat':30, 'Apples':200}
option=int(input("For list of items press 1:"))
if option==1:
    print(list)
for i in range(len(items)):
    inp1=int(input("If you want to buy press 1 or 2 for Exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter Your Items:")
        quantity=int(input("Enter the quantity:"))
        if item in items.keys(): 
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*6)/100
            finalamount=gst+totalprice
        else:
            print("Sorry You Entered item is not Available:")
    else:
        print("You entered wrong number")
    inp=input("Can I generate the items Yes or No:")
    if inp=='Yes':
        pass
        if finalamount!=0:
            print(25*"=", "Karun's SuperMarket",25*"=")
            print(28*" ","Tanuku")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("S.no",6*" ",'items',6*" ",'Quantity',3*" ",'Price')
            for i in range(len(plist)):
                print(i,6*' ',6*' ',ilist[i],3*' ',qlist[i],plist[i])
                print(75*"-")
                print(50*" ",'TotalAmount:','Rs',totalprice)
                print("gst amount",50*" ",'Rs',gst)
                print(75*"-")
                print(50*" ",'finalamount:','Rs',finalamount)
                print(75*"-")
                print(50*" ","Thanks For Visiting")
                print(75*"-")



                

    


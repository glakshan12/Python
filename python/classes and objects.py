'''class goa:
    name=""
    drink=""
    def party():
        print("lets party")
    def beach():
        print("enjoying the beach")
laksh=goa()
laks=goa()
laksh.name="Laksh"
laks.name="Laks"
laksh.drink="yes"
laks.drink="no"
print(laksh.name)
print(laks.name)
print(laksh.drink)
print(laks.drink)
laksh.party()
laks.beach()

#

class laptop:
    price=""
    processor=""
    ram=""
hp=laptop()
dell=laptop()
lenevo=laptop()
hp.price="40000"
hp.processor="ryzen"
hp.ram="8"
dell.price="40000"
dell.processor="intel"
dell.ram="8"
lenevo.price="40000"
lenevo.processor="ryzen5 5500U"
lenevo.ram="8"
print(hp.price,hp.processor,hp.ram)
print(dell.price,dell.processor,dell.ram)
print(lenevo.price,lenevo.processor,lenevo.ram)

class laptop:
    def __init__(self,price,processor,ram):
        self.price=price
        self.processor=processor
        self.ram=ram
    def __str__(self):
            return f"\nprice:{self.price}\nprocessor:{self.processor}\nram:{self.ram}"
hp=laptop("40000","ryzen 5","8gb")
print(hp)'''

#

    
       
        

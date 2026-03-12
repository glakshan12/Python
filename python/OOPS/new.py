""" class mobile:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
m1=mobile("vivo","v2065")
m2=mobile("lenevo","ideapadslim1")
print(m1.brand)
print(m2.model)

class car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
c1=car("toyoto","Fortuner",2005)
c2=car("maruti suzuki","Alto",2009)
c3=car("tata","Punch",2020)
print(c1.brand)
print(c2.model)
print(c3.year)

class bank:
    branch="thingalur"
    def __init__(self,acname,deposit,balance):
        self.acname=acname
        self.deposit=deposit
        self.balance=balance
    def display(self,withdraw):
        self.withdraw=withdraw
        balance=deposit-withdraw
        print(f"the balance is {balance} of account 1")
ac1=bank("Lakshan",5000)
ac2=bank("Laksh",10200) """

class Mobile:
    def __init__(self,name,marks):
        self.marks=marks
        self.name=name
    def add_marks(self,mark):
        self.marks+=mark
    def get_marks(self):
        return self.marks
s1=Mobile("Lakshan",70)
s1.add_marks(10)
print(s1.get_marks())
        
'''types of variable in class,functions are told as methods
class variable and instance variable and local variables
instance variable is a self constructor which is created inside function
class variable is create after class


class phone:
    charger="ctype"#class variable
    def __init__(self,brand,price):
        self.brand=brand#instance variables
        self.price=price
    def display(self):
        print(self.brand)
        print(self.price)
        print(self.charger)
phone.charger="btype"
vivo=phone("v20","15000")
vivo.display()'''

#class methods
whereever function is created with self method is instance method

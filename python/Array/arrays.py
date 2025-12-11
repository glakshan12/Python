#python does not have built in array instead of use list
#to work with python array need to import library like numpy 

car1=["BMW"]
car2=["VOLVO"]
car3=["ROLLS ROYCE"]
cars=["FERRARI","JAQUAR","LAMBORGHINI"]
print(car1[0])
for x in car2:
    print(x,end="")
print()
print(len(car3))
car1.append("HONDA")
car1.remove("BMW")#pop also use
print(car1)
cars.sort(reverse=True)#sorting is only for multiple elements
print(cars)
car1.sort(reverse=True)
print(car1)
def mycar(e):
    return len(e)
car=["FERRARI","JAQUAR","LAMBORGHINI"]
car.sort(key=mycar)
print(car)
#sort a list of dict 
def dicti(e):
    return (e)#(e["year"])
car4=[
    {"car":"ford","year":2005},
    {"car":"bmw","year":2003},
    {"car":"VW","year":2000},
]
car4.sort(key=lambda e:e["year"])
print(car4)
'''class laksh:
    def __init__(self):
        print("display")
hp=laksh()
#
class laksh:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def __str__(self):
        return f"\nname:{self.name}\nage:{self.age}\ngender:{self.gender}"
laks=laksh("Laksh","20","male")
print(laks)'''

#
""" class employee:
    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=int(salary)
    def show_details(self):
        print(f"\nname:{self.name},\nposition:{self.position},\nsalary:{self.salary}")
    def apply_raise(self,percent):
        amt=self.salary*(percent/100)
        self.salary=self.salary+int(amt)
    def __str__(self):
        return f"employee{self.name},{self.position},{self.salary}"
emp=employee("laksh","hacker","50000")
print(emp)
emp.show_details()
emp.apply_raise(20)
emp.show_details() """

# class laksh:
#     pass

#
class student:
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
    def display(self):
        print(f"{self.name}\n{self.regno}")
    def __str__(self):
        return f"{self.name}\n{self.regno}"
s1=student("laksh","730922104069")
s1.display()
print(s1)#automatically uses a __str__ method

"""class fruit:
    def __init__(self,col):
        self.color=col
apple=fruit("red")
print(apple.color)

class Teacher:
    def __init__(self, name, regno):
        self.name = name
        self.regno = regno
    def display(self, tname, tregno):
        self.tn = tname
        self.tr = tregno
    def __str__(self):
        tn = getattr(self, "tn", "n/a")  # if tn not set, default = "n/a"
        tr = getattr(self, "tr", "n/a")  # if tr not set, default = "n/a"
        return f"{self.name}\n{self.regno}\n{tn}\n{tr}"
t1 = Teacher("laksh", "123")
t2 = Teacher("arun", "456")
t2.display("laks", "12")
print("Teacher 1:")
print(t1)   # tn and tr not set, so will print n/a
print("\nTeacher 2:")
print(t2)   # tn and tr set, so prints them


#
class teacher:
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
    def display(self):
        print(self.name)
        print(self.regno)

t1=teacher("laks","123")
t2=teacher("laksh","124")
t1.display()
t2.display()'''

#
'''class calculator:
   def __init__(self,a,b):
       self.a=a
       self.b=b
   def add(self):
       print(self.a+self.b)
   def sub(self):
       print(self.a-self.b)
obj=calculator(10,20)
obj.add()
obj.sub()'''
"""
       
        
    

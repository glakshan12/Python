""" color=("red","blue","green","black")
print(color[1:3])
n=(2,4,6,8,10)
a=len(n)//2
print(n[a])
city=("london","adelaide","chennai","bengaluru","edinburgh")
print(city[2])
print("red" in color)
b=("cat","dog")
c=("lion","tiger")
d=b+c
print(d)
tup=(1,2)
print(tup*2)
t=(5,10,15,20,25)
print(len(t))
tuples=(100,)
print(type(tuples)) """


""" animal=("dog", "cat", "lion", "tiger", "elephant")
print(animal[0])
print(animal[-1])
element=(10, 20, 30, 40, 50, 60)
print(element[2])
print(element[4:])
fruits=("london","adelaide","chennai","bengaluru","edinburgh","melbourne","erode")
print(fruits[2:6])
print(fruits[1:7])
q=("A", "B", "C", "D", "E")
p=len(q)//2
print(q[p])
print(q[:3])
color=("red", "green", "blue")
print(color)
num=(100,200,300,400)
w=len(num)//2+1
print(num[w]) """

""" data = ("apple", (10, 20, 30), "banana")
# Q: Print the number 20 from inside the nested tuple.
print(data[1][1])
students = (("John", 25), ("Alice", 22), ("Bob", 30))
# Q: Print "Alice" and her age 22.
print(students[1])
print(students[1][0])
print(students[1][1])
person="laksh",25,"india"
name,age,country=person
print(name)
print(age)
print(country) 
colors = ("red", "green", "blue", "yellow")
# Q: Print each color with its index number.
# Example: 0: red, 1: green ...
for i,color in  enumerate(colors):
    print(i,color)
marks = {"math": (80, 90, 100), "science": (70, 85, 95)}
# Q: Print the last mark in "science".
print(marks["science"][-1])
print(f"{marks["science"][-1]}")
"""
""" 
student=("john",20,"A++")
name,Age,Grade=student
print(student)
data = ("Alice", 25, "Female", "Engineer")
# Q: Unpack only name and profession, ignore other
name,_,_,profession=data
print(name,profession)
a,b=5,10
a,b=b,a
print(a,b)

nums=(1,2,3,4,5)
x,*mid_lis,y=nums
print(x)
print(mid_lis)
print(y)

students = [("John", 25), ("Alice", 22), ("Bob", 30)]
# Q: Print "Name: ___, Age: ___" for each student using unpacking
for name,age in students:
    print(f"{name} is {age} years old")

def rectangle(a,b):
    return(a*b,2*(a+b))
area,perimeter=rectangle(5,10)
print(area)
print(perimeter)

person=("David",(30,"engineer"))
name, (age,profession)=person
print(name)
print(age)
print(profession)

a= ("Python", "Java", "C++", "Go", "Rust")
b,*_,c=a
print(b)
print(c)
 """
data = ("Alice", 24, "A+")
name,age,grade=data
print(name,age,grade)
d = ("Bob", 22, "Male", "Student")
name,_,_,profession=d
print(name,profession)
x,y=5,10
x,y=y,x
print(x,y)
numbers = (1, 2, 3, 4, 5, 6)
a,*mid,b=numbers
print(a,mid,b)
students = [("John", 25), ("Alice", 22), ("Bob", 30)]
for name,age in students:
    print(f"name:{name}, age:{age}")
def calc(a,b):
    return(a+b,a-b,a*b)
sum,diff,prod=calc(5,10)
print(sum,diff,prod)
person = ("David", (30, "Engineer"))
name,(age,profession)=person
print(name)
print(age)
print(profession)
data = ("Python", "Java", "C++", "Go", "Rust")
a,*_,b=data
print(a,b)
datas = ("Alice", (10, 20, 30), "Bob")
n=list(datas)
(a,*numbers,b)=datas
print(a)
print(b)
print(numbers)
print(n)
print(datas)
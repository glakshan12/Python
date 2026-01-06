""" #singlelevel inheriance
class animal:
    def dog(self):
        print("bark")
class animal2(animal):
    def cat(self):
        print("meow")
d=animal2()
d.dog()
d.cat()

#multilevel inheritance
class a:
    def inn(self):
        print("def")
class b(a):
    def inn2(self):
        print("inn")
class c(b):
    def inn3(self):
        pass
d=c()
d.inn()
d.inn2()
d.inn3()

#multiple inheritance
class a:
    def p(self):
        print("1")
class b:
    def m(self):
        print("2")
class c(a,b):
    def ch(self):
        pass
d=c()
d.ch()
d.m()
d.p()

#hybrid inheritance
class a:
    def eat(self):
        print("eat")
class b(a):
    def eats(self):
        print("eats")
class c(a):
    def eating(self):
        print("eating")
house=a()
house.eating() """


""" class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class salary(employee):
    def __init__(self,basic):
        self.basic=basic
        print(f"name is {self.name} , id is {self.id} and basic salary is{basic.salary}")
        super().show()
s=salary()
s(name="lakshan",id=123,basic=50000) """



""" n=5
arr=[4,6,9,3,7]
for i in arr:
   if i<2:
    continue
      
   isprime=True
   for j in range(2,i):
          if i % j==0:
            isprime=False
            break
   if isprime:
      print(i) """

""" class animal:
    def __init__(self):
        print("ok")
class dog(animal):
    def __init__(self):
        print("good")
        super().__init__()
d=dog()

class person:
    def walk(self):
        print("walking")
class student(person):
    pass
d=student()
d.walk()

class vehicle:
    def __init__(self):
       self. wheels=4
class car(vehicle):
    pass
w=car()
print(w.wheels)

class animal:
    def __init__(self):
        print("animal created")
class dog(animal):
    def __init__(self):
        super().__init__()
        print("dog created")
a=dog()

class employee:
    def get_role(self):
        print("employee")
class manager(employee):
    def get_role(self):
        super().get_role()
        print("manager")
d=manager()
d.get_role()

class grand:
    def __init__(self):
        print("house")
class parent(grand):
    def __init__(self):
        print("car")
        super().__init__()
class child(parent):
    def __init__(self):
        print("cycle")
        super().__init__()
b=child() """

#diamond pattern
n=4
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for s in range(1,2*i):
        print("*",end=" ")
    print()

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(n,1,-1):
    for j in range(1,i):
        print("*",end=" ")
    print()

arr=[1,2,3,4]
x=3 #in check inside containers only not single element 
for i in range (len(arr)):
    if arr[i]==x:
        print(i)
if arr[i]!=x:
    print("-1")

arr=[1,2,3,4,5]
a=arr[-1:]+arr[:-1]
print(a)#arr[:] means shallow copy of same array

arr= [12, 35, 1, 10, 34, 1]
lar=float('-inf')
sec=float('-inf')
for i in arr:
    if i>lar:
        sec=lar
        lar=i
    elif i <lar and i>sec:
        sec=i
print(sec)

""" arr=[12,35,1,10,24,1]
lar=float(-'inf')
sec=float(-'inf')
third=float(-'inf')
for i in arr:
    if i>lar:
        sec= """

a=set([1,2,3,4,5])
b=set([1,2,3])
print(b .issubset(a))

a={1,2,3,4,5}
b={1,2,3}
print(a.issubset(b))

#tdy
a=[1, 4, 3, -5, -4, 8, 6]
lar=float("-inf")
smallest=float("inf")
for num in a:
    if num>lar:
        lar=num
    if num<smallest:
        smallest=num
print(lar)
print(smallest)

arr=[15,0,2,4,7]
for i in range(len(arr)):
    if i==arr[i]:
        print(arr[i])

n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for s in range(2*i-1):
        print("*",end=" ")
    for k in range(n-i):
        print(" ",end=" ")
    print()
for i in range(n,0,-1):
    for s in range(n-i):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
    for k in range(n-i):
        print(" ",end=" ")
    print()


n=4
for i in range(1,n+1):
    if i%2==1:
        val=1
    else:
        val=0
    for j in range(i):
        print(val,end=" ")
        val=1-val
    print()
print()

""" n=4
for i in range(1,n+1):
    if i<=2 and i%2==1:
        val=1
    else:
        val=0
    while i>3:
     if i%2==1:
        val=0
     else:
            val=1
    for j in range(i):
        print(val,end=" ")
        val=1-val
    print() """


#reverse an array using two pointers
arr=[1,2,3,4]
l=0
r=len(arr)-1
if l<r:
    arr[l],arr[r]=arr[r],arr[l]
    l=l+1
    r=r-1
print(arr)


#frequency count
arr=[1,2,3,2,2,4]
x=2
count=0
for i in arr:
    if i ==x:
        count+=1
print(count)

#find duplicate
arr=[1,2,3,2,4,1]
freq=[]
duplicate=[]
for i in arr:
    if i in freq:
        duplicate.append(i)
    else:
        freq.append(i)
print(duplicate)

#move the zeros to one end
arr=[0,1,0,3,12]
pos=0
for i in range(len(arr)):
    if arr[i]!=0:
        arr[i],arr[pos]=arr[pos],arr[i]
        pos=pos+1
print(arr)

#missing number in array
arr=[1,2,4,5]
n=5
sum=n*(n+1)//2
count=0
for i in arr:
    count+=i
missed=sum-count
print(missed)


#sum the number using recursion
def sum_digits(n):
    if n <= 0:          # base case
        return 0
    return (n % 10) + sum_digits(n // 10)
sum_digits(123) 

#reverse the number using recursion
def rev(n,result):
    if n==0:
        return result
    digits=n%10
    return rev (n//10, result*10+digits)
print(rev(1234,0))

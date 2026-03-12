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
""" n=4
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

arr=[12,35,1,10,24,1]
lar=float(-'inf')
sec=float(-'inf')
third=float(-'inf')
for i in arr:
    if i>lar:
        sec=

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
print() """

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
""" arr=[1,2,3,4]
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
arr=[0,1,0,3,12]#
pos=0
for i in range(len(arr)):
    if arr[i]!=0:
        arr[i],arr[pos]=arr[pos],arr[i] #[1,3,12,0,0]
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


n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print()


n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for s in range(i):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for s in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

n=3
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    for s in range(2*n-2*i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()

n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(ord("A")+j-1),end=" ")
    print()

arr=[2,3,5,4,1]
arr.sort(reverse=True)
print(arr)

#check if array is sorted or not?
arr=[2,4,8,6,10]
is_sorted=True
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        is_sorted=False
        break
if not is_sorted:
    print(is_sorted)

arr=[10,8,6,4,2]
descending=True
for i in range(len(arr)-1):
    if arr[i]<arr[i+1]:
        descending=False
        break
print(descending)

#reverse an array
arr=[1,2,3,4,5]
l=0
r=4
while l<=r:
    arr[l],arr[r]=arr[r],arr[l]
    l+=1
    r-=1
print(arr)

#find if array is consecutive or not
arr=[4,2,3,5,1]
consecutive=True
max=5
min=1
if max-min+1!=len(arr):
    consecutive=False
print(consecutive)

#find the missing positive integer need to check this
arr=[3,4,-1,1,1]
b=set()
n=4
sum=n*(n+1)//2
count=0
for i in arr:
    if i>0:
        b.add(i)
for i in b:
    count=count+i
missed=sum-count
print(missed)

def a(n):
    if n<=0:
        return 0
    return (n%10)+a(n//10)
print(a(12345))

#sum of n natural numbers
def b(n):
    if n==1:
        return 1
    return(n)+b(n-1)
print(b(5))

#count the no of digits using recursion
def c(n):
    if n==0:
        return 0
    return 1+c(n//10)
print(c(12345))

#power the number 
def num(n,m):
    if m==0:
        return 1
    return n*num(n,m-1)
print(num(2,3)) """

""" arr=[1,2,3,4,3]
k=6
count=0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i]+arr[j]==k:
            count+=1
print(count)


arr=[1,2,3,4,3]
k=6
c=0
seen={}
for i in arr:
    if k-i in seen:
        c+=1
    seen[i]=1
print(seen)
print(c)


#return true if first occurance is k
arr=[10,15,3,7]
k=17
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==k:
            print("true")
            break

#return count pair equal to k
arr=[-1,1,2,-2,3]
k=0
count=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==k:
            count+=1
print(count)

#return pair equal to k
arr=[1,5,7,-1,5]
k=6
seen=set()
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==k:
            pair=tuple(sorted((arr[i],arr[j])))
            if pair not in seen:
                seen.add(pair)
                print(pair)

#return total sum of elements
def total(n):
    if n==[]:
        return 0
    return n[0]+total(n[1:])
arr=[1, 2, 3, 4, 5]
result=total(arr)
print(result)
 """

""" n=3
for i in range(1,n+1):
    for j in range(i,n):
        print("1",end=" ")
    for s in range(1):
        print("*",end=" ")
    for k in range(n-i):
        print("1",end=" ")
    for m in range(1):
        print("*",end=" ")
    print() """

""" arr=[7,8,-1,9,1]
b=set()
n=len(arr)
for i in arr:
    if i>0:
        b.add(i)
print(b)
for i in range(1,n+1):
    if i not in b:
        print(i)
        break

arr=[1,2,3,1,2,6,6,4]
n=[]
seen=[]
for i in arr:
    if i not in n:
        n.append(i)
    elif i not in seen:
        seen.append(i)
print(n)
print(seen)

arr=[1,2,3,5,4,5,1]
n=[]
m=[]
for i in arr:
    if i not in n:
        n.append(i)
    elif i in n:
        print (i)
        break

arr=[0,1,0,3,12]
p=0
for i in range(len(arr)):
    if arr[i]!=0:
        arr[i],arr[p]=arr[p],arr[i]
        p+=1
    print(arr)
print("after traverse the zeros",arr)

#palindrome check
def palindrome(s):
    if s=="":
        return True
    elif s[0]!=s[-1]:
        return False
    return(palindrome(s[1:-1]))
print(palindrome("madam"))

a=[1,2,3,4,5]
print(a[1:-1])
print(a[1:3]+a[3:4])

s="madam"
print(s[::-1])
c=0
for ch in s:
    if ch in s:
        c+=1

def a(arr):
     if arr==[]:
        return True
     elif arr[0]>arr[len(arr)-1]:
        return False
     return a(arr[1:])
print(a([1,2,3,4,5]))

n=3
for i in range(1,n+1):
    for j in range(i,n):
        print("1",end=" ")
    for s in range(1):
        print("*",end=" ")
    for k in range(i-1):
        print("1",end=" ")
    for m in range(i-1):
        print("*",end=" ")
    print()
print()

n=4
for i in range(n,0,-1):
    for s in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print() """

#2d array
#col wise sum
""" matrix=[[1,2,3],
        [4,5,6]]
for j in range(len(matrix[0])):
    c=0
    for i in range(len(matrix)):
        c=c+matrix[i][j]
    print(c)

for j in range(len(matrix[0])):
    col_sum = 0
    for i in range(len(matrix)):
        col_sum = col_sum + matrix[i][j]
    print("Column", j, "sum =", col_sum)

#print array
arr=[[1,2,3],
     [4,5,6]
     ]
print(arr)

#row wise print
arr=[[1,2,3],
    [4,5,6]]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j],end=" ")
    print()

#row wise sum
arr=[[1,2,3],
    [4,5,6]]
for i in range(len(arr)):
    count=0
    for j in range(len(arr[i])):
        count=count+arr[i][j]
    print("row",i,"sum",count)

#coloumn wise sum
arr=[[1,2,3],
    [4,5,6]]
for j in range(len(arr[0])):
    c=0
    for i in range(len(arr)):
        c+=arr[i][j]
    print("col",j,"sum",c)

#maximun in 2d array
arr=[[1,2,3],
     [4,5,6]
     ]
maximum=float('-inf')
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] >maximum:
           maximum=arr[i][j]
print(maximum)


#minimum in 2d array
arr=[[1,2,3],
     [4,5,6]
     ]
minimum=float('inf')
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]<minimum:
            minimum=arr[i][j]
print(minimum)

#find element in 2d array
arr=[[1,2,3],
[4,5,6]]
x=3
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]==x:
            print(i,j)

arr=[[1,2,3],
[4,5,6]]
row1=float('-inf')
row2=float('-inf')
for i in range(len(arr)):
    row_sum=0
    for j in range(len(arr[i])):
        row_sum+=arr[i][j]
        if row_sum>row1:
            row1=row_sum
            row2=row1
        elif row_sum<row1 and row_sum>row2:
            row2=row_sum
print("row2",row2)


#pattern printing
n=6
for i in range(3,n+1):
   if i ==3:
       print(i,end=" ")
   else:
       print(i,end="")
       for j in range(3,i):
           print("*",i,end="")
   print()

#new pattern
print("code editor pattern")
n=6
for i in range(6,2,-1):
    if i==3:
        print(i,end=" ")
    else:
        print(i,end="")
        for j in range(3,i):
            print("*",i,end=" ")
    print()
for i in range(3,n+1):
   if i ==3:
       print(i,end=" ")
   else:
       print(i,end="")
       for j in range(3,i):
           print("*",i,end="")
   print()     

arr=[1,2,3,4,5]
k=3
print(arr[-k:]+arr[:-k])
print(arr[:k])

arr=[1,2,3,4,5]
k = 3
window_sum = sum(arr[:k])
max_sum = window_sum
for i in range(k, len(arr)):
    window_sum += arr[i] - arr[i-k]
    max_sum = max(max_sum, window_sum)
print(max_sum)


arr=[1,2,3,4,5]
max_sum = curr_sum = arr[0]
for i in range(1, len(arr)):
    curr_sum = max(arr[i], curr_sum + arr[i])
    max_sum = max(max_sum, curr_sum)
print(max_sum)

arr = [1, 2, 3, 2, 4, 1]
n = len(arr)
for i in range(n):
    for j in range(i+1,n):
        if arr[i]==arr[j]:
            print(arr[i])
arr = [1, 2, 3, 2, 4, 1]
b=[]
for i in arr:
    if i not in b:
        b.append(i)
    else:
        print(i)

arr = [1, 2, 3, 2, 4, 1]
freq={}
for i in arr:
    freq[i]=freq.get(i,0)+1
for key,value in freq.items():
    if value>1:
        print(key)

arr=[[1,2,3],
     [4,5,6],
     [3]]
total=float('-inf')
for i in range(len(arr)):
    row=0
    for j in range(len(arr[i])):
        row=row+arr[i][j]
    if row>total:
        total=row
print(total)


print("row wise sum with index")
arr=[[1,2,3],
     [4,5,6]]
count=0
max_row=0
for i in range(len(arr)):
    row=0
    for j in range(len(arr[i])):
        row+=arr[i][j]
    if row>count:
        count=row
        max_row=i
print(max_row)
print(count)

print("col wise sum with index")
arr=[[1,2,3],
     [4,5,6]]
count=float('-inf')
max_col=0
for j in range(len(arr[0])):
    col=0
    for i in range(len(arr)):
        col+=arr[i][j]
    if col>count:
        count=col
        max_col=j
print(max_col)
print(count)


print("diagonal")
arr = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]
n=len(arr)
diagonal=0
dia=0
for i in range(n):
    diagonal+=arr[i][i]
    dia+=arr[i][n-1-i]
print(diagonal)
print(dia)

arr = [-7, 1, 5, 2, -4, 3, 0]
left=0
total=sum(arr)
for i in arr:
    total=total-i
    if total==left:
       print(i)
       break
    left+=i

arr = [1, 3, 5, 2, 2]
left=0
total=sum(arr)
for i in range(len(arr)):
    right=total-left-arr[i]
    if left==right:
        print(i)
    left+=arr[i]

arr=[1,2,3,4,3]
k=6
c=0
seen={}
for i in arr:
    if k-i in seen:
        c+=1
    seen[i]=1
print(seen)
print(c) """

#print maximum subarray sum
nums = [5,4,-1,7,8]
current=0
maximum=float('-inf')
for i in nums:
    current+=i
    if current<i:
        current=i
    if current>maximum:
        maximum=current
print(maximum)

#print maximum subarray
arr=[-2,3,-1,2]
current=arr[0]
maximum=arr[0]
start=0
temp=0
end=0
for i in range(len(arr)):
    current+=arr[i]
    if current>maximum:
        maximum=current
        start=temp
        end=i
    if current<0:
        current=arr[i]
        temp+=1
print(maximum)
print(arr[start:end+1])

arr= [4, -1, 2, 1]
current=0
maximum=arr[0]
start=0#temp start
astart=0
end=0
for i in range(len(arr)):
    current+=arr[i]
    if current>maximum:
        maximum=current
        start=astart
        end=i
    if current<0:
        current=0
        start+=1
print("maximum:", maximum,arr[astart:end+1])
print(len(arr[astart:end+1]))


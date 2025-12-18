""" n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()
print()


n=4
for i in range(1 ,n+1):
    #row always taken current running iterate value only 
    for j in range(1,i+1):
        #in each condition it prints one star only and end is used for space
        print("*",end =" ")
        #print() used to start from new line
    print()
print()

n=4
for i in range(1,n+1):
    #this is python backward loop condition goes as 4,3,2,1 for each step -1(Start,stop,step)
    for j in range(4,i-1,-1):
        print("*",end=" ")
    print()
print()

n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print()

n=4
for i in range(1,n+1):
    for j in range(4,i-1,-1):#same number pattern in inverse order
        print(j,end=" ")
    print()
print()

n=4
for i in range(1,n+1):
    for j in range(1,n-i+2):#reverse number patterns
        print(j,end=" ")
    print()
print()


n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()
print()

#number add pattern
n=4
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+1
    print()
print()

n=4
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(" ",end=" ")
    print()
    for k in range(1,i):
        print("*",end=" ")
    for s in range(1,n-i+2):
        print(" ",end=" ")

n=5
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for s in range(1,i+1):
        print("* ",end="")
    print()
print()

n=5
for i in range(1,n+1):
    for j in range(1,i-1+1):
       print(" ",end="")
    for s in range(i,n+1):
        print("* ",end="")
    print()
print()
n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(ord("A")+j-1),end=" ")
    print()
print()

n=4
for i in range(1,n+1):
    for j in range(i,n+1):
        print(chr(ord("A")+j-1),end=" ")#if n-1 means it will print in letter in revrse order
    print()
print()

n=4
for i in range(0,n):
    for j in range(0,i+1):
        print(chr(ord("A")+i+1-1),end=" ")
    print()
print()

n=4
for i in range(1,n+1):
    for j in range(i,n+1):
        print(chr(ord("A")+i-1),end=" ")
    print()

#diamond pattern
n=5
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for s in range (1,i+1):
        print(" *",end="")
    print()
print()
n=5
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for s in range (i*2-1):
        print("*",end=" ")
    for k in range(1,n-i+1):
        print(" ",end=" ")
    print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print(" ",end=" ")
    for s in range(2*(n-i)-1):
        print("*",end=" ")
    for k in range(1,i+1):
        print(" ",end=" ")
    print() """
#count the no of digits 
""" n=58234
count=0
while n>0:
    n=n//10
    count=count+1
print(count)
#revrse the number
n=329
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
print(reverse)

#palindrome number
n=329
temp=n
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
if reverse==temp:
    print("palindrome")
else:
    print("not palindrome")
#palindrome string
n="lakshan"
reverse=n[::-1]
if reverse==n:
    print("palindrome")
else:
    print("not palindrome")

#divisors of a number 
n=12
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")
print()

a=12
b=18
gcd=0
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        gcd=i
print(gcd)

a=48
b=18
while b>0:
   a,b=b,a%b
print(a)

a=10
b=20
a,b=b,a
print(a,b)

n=10
for num in range(2,n+1):
    is_prime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
       print(num)

n = 10
for num in range(2, n+1):
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
    if not is_prime:
        print(num)

#last digit
a=739
b=82
c=a*b
last=0
while c>0:
    d=c%10
    last=last+d
    break
print (last)

a=739
b=82
c= (a*b)%10
print(c)
 """

fact=1
for i in range(5,0,-1):
    fact=fact*i
print(fact,end=" ")


def name(n):
    if n==0:
        return
    print("Lakshan") 
    return name(n-1) 
name(6)

def num(n):
    if n==5:
        return
    print(n)
    return num(n+1)
num(1)

def num(n):
    if n==0:
        return 
    print(n)
    return num(n-1)
num(5)

def num(n,sum=0):
    if n==0:
        print(sum)
        return
    num(n-1,sum=sum+n)
num(5) 


def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
    print(n)
fact(5)

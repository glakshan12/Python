""" """ #5*5 start pattern
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()
print()   

#number pattern
for i in range(4):
    for j in range(1,5):
        print(j,end=" ")
    print()
print()

#4 rows and increase coloumn
for i in range(4):
    for j in range(0,i+1):#coloumn increases 
        print("*", end=" ")
    print()
print()

for i in range(1,6):#connect the coloumn to row is imp for this pattern
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print()

#same number in each coloum and row
for i in range(1,6):
    for j in range(1,i+1):
        print(i, end=" ")
    print()
print()

#reverse pattern
for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()
print()

#reverse number pattern
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print()

#pyramid pattern
for i in range(5):
    for j in range(4-i):
        print(" ",end=" ")
    for k  in range(2*i+1):
        print("*",end=" ")
    for s in range(4-i):
        print(" ",end="")
    print()

print()

for i in range(5,0,-1):
    for j in range(5 - i):
        print(" ", end=" ")
    for k in range(2*i - 1):
        print(i, end=" ")
    for s in range(5-i):
        print(" ",end=" ")
    print()
print()

#diamond pattern
for i in range(1,6):
    print(" " * (5-i)+"*" * (2*i-1))
for j in range(5,0,-1):
    print(" " * (5-j)+"*" *(2*j-1))
print()

#pattern 10
for i in range(4):
    for j in range(0,i+1):
        print("*",end=" ")
    print()
for k in range(4,0,-1):
    for j in range(0,k):
        print("*",end=" ")
    print()
print()
#pattern 10.1
for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()
print()
#pattern 11
start=1
for i in range(5):
    if i%2==0:
        start=1
    else:
        start=0
    for j in range(0,i+1):
        print(start,end=" ")
        start=1-start
    print()
print()
#pattern 12
for i in range(4):
    for j in range(1,i+2):
        print(j,end=" ")
    for k in range(2*(4-i-1)):
        print(" ",end=" ")
    for s in range(i+1,0,-1):
        print(s,end=" ")
    print()
print()
#pattern13
n=1
for i in range(6):
    for i in range(1,i+1):
        print(n,end=" ")
        n=n+1
    print()
print()
#patter 14
for i in range(5):
    for j in range(0,i+1):
       print(chr(65+j),end=" ")
    print()
print()
#pattern 15
for i in range(5,0,-1):
    for j in range(0,i):
        print(chr(65+j),end=" ")
    print()
print()
#pattern16
for i in range(5):
    for j in range(0,i+1):
        print(chr(65+i),end=" ")
    print()
print()

#pattern17
for i in range(5):
    for j in range(4-i):
        print(" ",end=" ")
    ch=65
    for k in range(2*i+1):
        print(chr(ch),end=" ")
        if k<i:
            ch+=1
        else:
            ch-=1
    for s in range(4-i):
        print(" ",end=" ")
    print()

n=5
sum=0
while n<=n:
    sum=sum+n
    n=n+1
print(sum)
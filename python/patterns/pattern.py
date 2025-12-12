#5*5 start pattern
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

for i in range(1,6):#connct the coloumn to row is imp for this pattern
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
    for j in range(5-i):
        print(" ",end=" ")
    for k  in range(2*i+1):
        print("*",end=" ")
    for s in range(5-i):
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



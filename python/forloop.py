""" for i in range(1,11):
    print(i,"x2=",i*2)
 """
""" #examples
a=8
b=15
for i in range(a+1,b):
    print(i) """

#ex2
""" for i in range(1,11):
    if(i%2==0):
       print(i) """
       


"""#ex3
for i in range(1, 51):                                
    if(i % 3 == 0 and i % 5 == 0):    
        print("fizzbuzz")
    elif(i % 3 == 0):
        print("fizz")
    elif(i % 5 == 0):
        print("buzz")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

#ex4
count=0
for i in range(1,11):
    if(i%2==0):
        count=count+1
print(count)

#ex5
count=0
for i in range(1,11):
    if(i%2!=0):
        count=count+1
print(count)"""


#ex6
"""e_count=0
o_count=0
for i in range(1,11):
    if(i%2==0):
        e_count=e_count+1
    else:
        o_count=o_count+1
print(e_count)
print(o_count)"""


#ex7
""" count=0
for i in range(1,101):
    if(i%3==0 and i%5==0):
        count=count+1
print(count) """

"""#sum of naturl numbers
sum=0
for i in range(1,6):
    sum=sum+i
print(sum)"""

#ex[list in forloop)include all values within squarebracket]
""" a=[]
print("enter 5 number")
for i in range(5):
    num=int(input("enter num"+str(i+1)))#casting for converting integer to string
    a.append(num)
print(a)

sum=0
for i in a:
    sum=sum+i
print(sum) """


 
#
num=7
sum=0
for i in range(1,num+1):
    print(i,end=' ')
    sum=sum+i
print()
print("sum=",sum)

#
for i in range(1,6):
    cube = i**3
    print("number is:",i," and cube of the", i, "is:",cube)

for i in range(7):
    if i==4:
        break
    print(i)
for i in range(6):
    if i==3:
        continue
    print(i)
for i in range(5):
    if i==5:
        pass
    print(i)

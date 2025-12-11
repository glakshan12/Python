
'''#nestedif
x = 10
if x > 0:
    if x < 20:
        print("x is between 1 and 19")

#test
#test2
score=85
submit_certificates="yes"
if(score==85):
    print("enter your exam score",score)
    if(submit_certificates=="yes"):
        print("have you submit all certificates?",submit_certificates)
        if(score>80):
            print("admission approved")
        else:
            print("not approved") 

#test3
income=int(input())
if(income<70000):
    print("scholarship is available")
else:
    print("not eligible for scholarship")

#test4 binaryoperator used(and,or,not)
income=int(input())
if(income>7000):
    print("scholarship is available")
else:
    print("not eligible for scholarship")'''

#test5binaryoperator used(and,or,not)
a=int(input())
if(a%3==0 and a%5==0):
    print("yes")
else:
    print("no")

'''#test6(not nestedif)
score=100
if(score<35):
    print("poor student")
elif(score>35 and score<70): #(score>35 and score<70)(also use elif condition)
    print("average student")
elif(score>70 and score<100):
    print("moderate student")
else:#use if condition also
    print("invalid")

#mini calculator
a=10
b=5
c=input("add/sub/mul/div")#ask user to choose an operation
if(c=="add"):
    print(a+b)
elif(c=="sub"):
    print(a-b)
elif(c=="mul"):
    print(a*b)
else:
    print(a/b)

#test8
p=80#Python doesn't allow the % symbol directly with numbers
if(p>70):
    a=input("enter your name:")
    b=input("department:")
    c=input("location:")
    print("eligible")
else:
    print("not eligible") '''

#test9
'''salary=25000
age=24
if(salary>=20000 or age<=25):
    a=int(input("required loan amount:"))
    if(a<=50000):
       print("eligible for loan")
    else:
       print("maximum amount loan is 50000")'''
       
#test10
a=55
b=56
c=57
d=58
e=59
f=(a+b+c+d+e)
avg=(f)/5
if(f<35):
     print("additional class required")
else:
     print("good to go")



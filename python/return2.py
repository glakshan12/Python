'''s_username="laksh"
s_password="123"
uname=input()
password=input()
def validate():
    if(s_username==uname and s_password==password):
        print("yes")
    else:
        print("no")
validate()'''
#
def add(n1,n2):
    return n1+n2
a=int(input())
b=int(input())
c=int(input())
d=add(a,b)
e=d*c
print(e)

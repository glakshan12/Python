num=10
print(num>0)

text=""
print(bool(text))

age=20
print(age>18)

num=45
print(num>40 and num<100)

items=[]
print(bool(items))

username="admin"
password="1234"
use=input("enter username")
pas=input("enter password")
if(use==username and pas==password):
    print("Login Succesfully")
else:
    print("invalid credentials")
    
import getpass
print("signup")
user=input("enter your name:")
p1=getpass.getpass("enter password:")
p2=getpass.getpass("enter password:")
if(p1==p2):
    print("signup succesfully")
else:
    print("password does not match")    
print("login")
name=input("enter your name:")
password=getpass.getpass("enter your password:")
if(name==user and password==p1):
    print("login succesfully")
else:
    print("invalid login credentials")
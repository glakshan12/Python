Sname=[]
while True:
    name=input("enter student name (or type'done' to finish):")
    if name.lower()=='done':
        break
    marks1=int(input("enter marks for s1:"))
    marks2=int(input("enter marks for s2:"))
    marks3=int(input("enter marks for s3:"))
    total=marks1+marks2+marks3
    percentage=(total/300)*100
    if(percentage>=90):
        print("Grade A")
    elif(percentage>=70):
        print("Grade B")
    elif(percentage>=50):
        print("Grade C")
    elif(percentage<50):
        print("Fail")
    
    
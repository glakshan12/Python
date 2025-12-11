""" numbers = (5, 10, 15, 20, 25, 30)
numbers=tuple(x for x in numbers if x!=15)
print(numbers[1:])
print(numbers[:-1])
print(numbers) """


student = ("John", 25, "Male", "A+")
students=list(student)
students[1]=students[1]+1
students.append("A++")
#students=student+("A++",)#append also
students.remove("Male")
#student=tuple(x for x in student if x!="male" )#use remove also
print(tuple(students))
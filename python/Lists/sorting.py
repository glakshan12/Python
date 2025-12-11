""" num=[12,5,8,3,15,1]
nums=num.copy()
nums.sort()
print(nums)
nums=sorted(num)
print(num)
a=sorted(num)
print(a)
b=sorted(a)
print(b) """



""" marks=[45,89,72,38,90,66]
mark=marks.copy()
mark.sort()
print(mark)
print(marks) """

""" names = ["john", "Alice", "Bob", "david"]
name=sorted(names)
print(name)
print(names)
n=sorted(names,key=str.lower)
print(n) """
""" 
numbers = [12, 5, 18, 7, 3, 25, 1]
number=numbers.copy()
number.sort(reverse=True)
print(number)
number=sorted(number)
print(number)
print(numbers)
 """


# Task:
# 1. Sort the list in ascending order (without changing original).
# 2. Sort the list in descending order (change original).
# 3. Print both results and the original list.
""" numbers = [12, 4, 19, 7, 2, 15]
number=numbers.copy()
number.sort()
print(number)
print(sorted(number,reverse=True))
print(numbers) """
#sorted is used in tuple

#in sort use just like num.sort(reverse=True) for sorted use like n=sorted(nums,reverse=True)
""" # Task:
# 1. Use sorted() and show normal sorting result.
# 2. Use sorted() with key=str.lower and show result.
# 3. Show the difference between original list and sorted result.
fruits = ["banana", "Orange", "apple", "Cherry"]
fruit =fruits.copy()
print(fruits)
print(sorted(fruit))
print(sorted(fruit,key=str.lower)) """



# Task:
# 1. Sort students by name.
# 2. Sort students by age.
# 3. Print original and sorted versions.
students = [("John", 25), ("Alice", 22), ("Bob", 30), ("David", 20)]
student=students.copy()
print(students)
student.sort()
print(student)
print(sorted(student,key=lambda student:student[1]))


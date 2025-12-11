'''data=[100,200,300,400]
data[1]=250
print(data)
a=[100,200,300,400]
a.append(500)
print(a)
b=[100,200,300,400]
b.insert(0,50)
print(b)
b.remove(300)
print(b)
b.pop()
print(b)'''



a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a[5]=99
print(a)
a.append(100)
print(a)
a.insert(0,0)
print(a)
a[0]=5  #replace
print(a)
num=[1, 2, 3, 4, 5, 6, 7, 8, 9]
nums=[i for i in num if i%2!= 0] #list comprehension
print(nums)

'''numbers=[1,2,3,4,5,6,7]
odd_numbers = []
for n in numbers:
    if n % 2 != 0:
        odd_numbers.append(n)
print(odd_numbers)


#replace
a=[1,2,3,4,5,6,7]
a[0]=5
print(a)'''
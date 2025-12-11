""" fruits={"apple","banana","Cherry"}
for x in fruits:
    print(x)

x={1,2,3,4,5}
for x in x:
   if(x%2==0):
        print("even")
   else:
        print("odd")

color={"red","green","black"}
for i,n  in enumerate(color):
    print(i,n)
    
n={10,2,3,4,5}
for n in sorted(n):
    print(n)
    
#add element while looping but in diff set
n={1,2,3,4,5}
add=[]
for i in n:
    if(i%2==0):
         add.append(i*10)
n.update(add)
print(n)

nums={1,2,3,4,5}
for n in nums.copy(): #direct modification in loop is error instead of this change into list and tuple
    if(n%2==0):
        nums.remove(n)
print(nums)

#set comprehension
nums={1,2,3,4,5}
odd={n for n in nums if n%2==1}
print(odd)

nums={1,2,3,4,5}
for n in list(nums):
    if n %2==0:#without copying refer line 30 for this
        nums.remove(n)
print(nums)

nums={1,2,3,4,5}
for n in list(nums):
    if(n%2==0):
        nums.remove(n)
        nums.add(n*10)
print(nums)"""

# Transform the Whole Set with Comprehension
nums={1,2,3,4,5}
nums={n if n%2 else n*2 for n in nums} #n is odd keep it as a n or if n is even replace with n*2
print(nums)

# Conditional Add & Remove Together
"""nums={1,2,3,4,5}
for n in list(nums):
    if n <3:
        nums.remove(n)
        nums.add(n**2)
print(nums) """

""" #problem 
nums = {2, 3, 5, 6, 7, 9, 10}
for n in list(nums):
    if n%3==0:
        nums.remove(n)
        nums.add(n**2)
print(nums)

nums = {2, 3, 5, 6, 7, 9, 10}
a=[]
for n in nums:
    if(n%2==0):
        a.append(n**2)
nums.update(a)
print(nums)


nums = {11, 4, 15, 2, 20, 5}
for n in list(nums):
    if n<10:
        nums.remove(n)
        nums.add(n**3)
print(nums) """

""" nums = {1, 2, 3, 4, 5, 6}
for n in list(nums):
    if(n%2==0):
        nums.remove(n)
        nums.add(n**2)
    elif(n%2!=0):
        nums.remove(n)
        nums.add(n**3)
print(nums) """

nums = {2, 3, 5, 6, 7, 8, 9}
for n in list(nums):
    if n %2==0:#use sorted only
        nums.remove(n)
        nums.add(n**2)
    elif(n%2!=0):
        nums.remove(n)
        nums.add(n**3)
print(nums)
print(sorted(nums,reverse =True))     
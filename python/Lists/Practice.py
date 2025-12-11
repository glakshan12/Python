""" a=[1,2,3,4,5]
for i in a:
    print(i)

b=[1,"laks",3.14,True]
print(b)
print([b[0],b[3]])#if uses two squres brackets means give in list
# print(f"Index 0: {b[0]}, Index 3: {b[3]}")
a=[1,2,3,4,5,6,7,8,9]
print(a[:3]+a[6:])
a.append("python")
print(a)
a[2]=100
print(a)
# a.remove(3)
print(a)
a.pop()
print(a)
print(len(a))
print(a.count(5))
 """
""" nums=[1,2,5,3,4]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

a=[1,2,3]
a.reverse()
print(a)
print(a.reverse())
b=[4,5,6]
a.extend(b)
print(a)
print(a+b)
c=[1,2,3]
d=[4,5]
print(c+d)
print(max(c))
print(min(c))
print(20 in c)
a=[1,2,3,4,5,6,7,8,9,10]
# b=[for  i in a if x%2!=0 i in b]
b=[]
for i in a:
    if i%2!=0:
        b.append(i)
print(b)
b=[i for i in a if i%2!=0]
print(b)
c=[]
for i in a:
    c.append(i*i)
print(c)
c=[i*i for i in a]#comprehension
print(c)
 """
#a from chatgpt
a=[]#print even numbers only
for i in range(51):
    if i %2==0:
        a.append(i)
print(a)#same
a=[i for i in range(51) if i%2==0]
print(a)

string=["Find", "the", "second", "largest", "number", "in", "a", "list"]
b=[i for i in string if len(i)>4 ]
print(b)#for len more than 4

a=[]
for i in range(101):
    if i>50:#for value above 50
        a.append(i)
print(a)
#create a list 1 to 100 using comprehension
a= [i for i in range(101)]
print(a)

a=[1,2,3,4,5,6,7,8,9,10]
largest=max(a)
a.remove(largest)
print(a[-1::])
a.sort()
print(a[-2])


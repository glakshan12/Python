s="laks"
s1=lambda s:s.upper()
print(s1(s)) # if function is not called means then it stores memory address

#map function
names = ["laksh", "ram", "sita"]
result=list(map(lambda names:names.upper(),names))
print(result)

#filter
nums = [2, 5, 7, 8, 3]
res=list(filter(lambda nums:nums>2,nums))
print(res)

#key
n=["laksh", "ram", "sita"]
r=sorted(n,key=lambda n:len(n))
print(r)
items = [
        (1, 3),#value 0,value 1
        (2, 1),
        (3, 2),#row is each tuple
        (7, 8),#coloumn is each element in tuple
]
results=sorted(items, key=lambda x: (x[1],x[1]))
print(results)

data = [
    (0, 2, 5),
    (1, 2, 3),
    (2, 1, 9),
    (3, 2, 3),
]

# sort by element at index 1, then by element at index 2
sorted_data = sorted(data, key=lambda x: (x[1], x[2]))
print(sorted_data)


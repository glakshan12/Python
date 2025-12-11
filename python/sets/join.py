""" set1={1,2,3}
set2={4,5,6}
set3=set1|set2
print(set3)

set1={1,2,3}#also join more than two sets
set2={4,5,6}
set3=set1.union(set2)
print(set3)

set1={1,2,3}#update() does not return anything
set2={4,5,6}
set3=set1.update(set2)
print(set3)
print(set1)

set1={1,2,3}
set1.add(4)
print(set1)

set1={1,2,3}
set1.remove(1)
set1.add(4)
set1.discard(3)
set1.update({5,6})
new=set1.union({7,8})
print(new)
print(set1)#except union all can modify the original for union new set is needed
set1.clear()
print(set1)
 """
#join setloop
""" set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}
join=set()
for s in [set1,set2,set3]:
    for item in s:
        join.add(item)
print(join)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}
join=set()
for s in [set1,set2,set3]:
    join.update(s)
print(join)

#set comprehension
join=set(item for s in [set1,set2,set3] for item in s)
print(join) """

"""nums = {10, 20, 30}

 # Step 1: create iterator from set
it = iter(nums)
#next can call repeatedly
# Step 2: fetch values one by one
print(next(it))  # first element (e.g., 10)
print(next(it))  # second element (e.g., 20)
print(next(it)) # third element (e.g., 30)

# Step 3: if we call again -> StopIteration error
# print(next(it))  
nums={10,20,30}
it=iter(nums)
for it in nums:
    print(it) """
    
#INTERSECTION
""" set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3=set1.intersection(set2)
print(set3)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1&set2)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.intersection(set2))

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3={6,7,5}
print(set1&set2&set3)
print(set1.intersection(set2&set3))

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.intersection_update(set2)
print(set1)
"""  """
set1 = {1, 2, 3}
set2 = {3, 4, 5}
join=set()
for  item in set1:
    if item in set2:
        join.add(item)
print(join)
    
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3={3,4,6}
join=set()
for  item in set1:
    if item in set2 and item in set3:
        join.add(item)
print(join)
    
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3={3,4,6}
join={x for x in set1 if x in set2 and x in set3}
print(join) """

#difference and symmetric difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3={3,4,6}
print(set1.difference(set2.union(set3)))
print(set1-set2)
join={x for x in set1 if x not in set2}
print(join)

""" set1 = {1, 2, 3} 
set2 = {3, 4, 5}
set3={3,4,6}   #sd only accept single argument at a time but in union and inter it works(set1,set2)
print(set1.symmetric_difference(set2).symmetric_difference(set3))
print(set1^set2^set3)
join={s for s in set1.union(set2) if s not in set1.intersection(set2)}
print(join) """
#for 3 sets use union 2 times and use intersection  2 times or .unio(set1,set2)
""" A = {1, 2, 3, 4, 5, 6}#cricket
B = {4, 5, 6, 7, 8}#football
C = {6, 7, 8, 9}#hockey
print(A.intersection(B))
print(A.intersection(B,C))
print(A.difference(B,C))
print(A.union(B,C))
print(A&B-C|B&C-A|C&A-B) """

"""python={101,102,103,104}
java={103,104,105,106}
c={104,106,107}
print(python.intersection(java))
print(python.intersection(java,c))
print(python.difference(java.union(c)))
print(python.symmetric_difference(java))
print(python.union(java,c))""" 

"""f= {101, 102, 103, 104, 105}
s= {104, 105, 106, 107}
h= {105, 107, 108, 109}
print(f.intersection(s))
print(f.intersection(s,h))
print(f.difference(s,h))
print(f.symmetric_difference(h))
print(f&s-h|s&h-f|h&f-s)
print(f|s|h)""" 


""" A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}
print(A|B)
print(A&B)
print(A-B)
print(A^B)

x = {10, 20, 30, 40}
y = {20, 30, 50}
z = {30, 60, 70}
print(x.intersection(y,z))
print(x|y-z)
print(x&y-z|y&z-x|z&x-y)

p={101, 102, 103, 104, 105}
j={104, 105, 106, 107}
d={105, 107, 108}
print(p.intersection(j,d))
print(p.difference(j,d))
print(p|j|d)
print(p&j-d|j&d-p|d&p-j) """
 
"""nums={1,2,3,4,5,6,7,8,9,10}
n={n if n%2 else n**2 for n in nums}
print(n)

nums={1,2,3,4,5,6,7,8,9,10}
n={n for n in nums if n%2==0}
print(n)

nums={1,2,3,4,5,6,7,8,9,10}
n={n**2 for n in nums if n%2==0}
print(n)

nums={1,2,3,4,5,6,7,8,9,10}
n={n**2 for n in nums if n%2!=0}
print(n)

fruits={"apple","banana","cherry"}
fruits.add("orange")
fruits.update(["grape","melon"])
print(fruits)""" 

A = frozenset({1, 2, 3})
B = frozenset({2, 3, 4})
print(A.intersection(B)) 
#frozenset is justlike a set which is immutable
#cant add ,remove or any change in its
#hashable->used as an key in dict or as an element inside another set (normal set cant)
"""fs=frozenset([1,2,3,4])
print(fs)
f=frozenset(['hello'])
print(f)
A=frozenset([1,2,3])
B=frozenset([4,5,6])
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))
d={A:"firstset", B:"secondset"}
print(d)"""

""" f=frozenset([10,20,30,40,50])
print(f)
fs=frozenset("apple")
print(fs)
#  fs.add("banana")
# print(fs) 
frozen=(1,2,2,3,4,3)
f=frozenset(frozen)#create tuple
print(f)
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5,6])
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))
groups={
    frozenset(["Alice","Bob"]):"Team1",
    frozenset(["Laksh","great"]):"Team2"
    
}
print(groups[frozenset(["Laksh","great"])])
print(groups[frozenset(["Alice","Bob"])]) """ 

# """ Elements of a set/frozenset must be hashable (immutable).
# (3,4) is a tuple → immutable → hashable → ✅ allowed.
# [3,4] is a list → mutable → ❌ not allowed. """
# ou cannot directly make a frozenset from a list of lists, because lists (["A","B"]) are mutable and unhashable. Frozenset requires elements that are hashable (like strings, tuples, frozensets).
groups_list = frozenset([("A", "B"), ("C", "D"), ("B", "A"), ("E", "F")])
print(groups_list)
# Demonstrate that frozenset treats ("A", "B") and ("B", "A") as distinct elements
print(("A", "B") in groups_list)  
print(("B", "A") in groups_list)  
print(("C", "D") in groups_list)  
print(("F", "E") in groups_list)  

groups = [["A", "B"], ["C", "D"], ["B", "A"], ["E", "F"]]
group={}
for g in groups:
   group[frozenset(g)]="Same"
print(group)

x = frozenset([1, 2, (3, 4)])
print(x)#not allowed list here

receipe={
   frozenset(["idly","Dosa","vadai"]):"Rice",#key:value 
   frozenset(["cake","biscuits","cream"]):"Fast"
}
print(receipe[frozenset(["idly","Dosa","vadai"])])

""" a=frozenset[(1,2,4)]
b=frozenset[(2,3,4)]
c=frozenset[(4,5,6)]
print(a.intersection(b,c))
 """
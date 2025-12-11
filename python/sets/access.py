"""fruit={"apple","banana","cherry"}
print(fruit)
a=set(["apple","banana","cherry"])
print(a)
empty=set()
print(empty)

fruit={"apple","banana","cherry"}
for x in fruit:
    print(x)"""
    

"""fruit={"apple","banana","cherry"}
print("apple"in fruit)
print("grapes"in fruit)
print("apple" not in fruit)

fruit={"apple","banana","cherry"}
fruits=list(fruit)
fruitss=tuple(fruit)
print(fruits)
print(fruitss)"""
"""fruit={"apple","banana","cherry"}
words=[word[0]for word in fruit]
# for word in fruits:
    # words.append(word[0]) 
print(words)"""

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
fruits.update(["cheese","apple","perry"])
print(fruits)
fruits.remove("apple")
print(fruits)
fruits.discard("cheese")
print(fruits)
fruit=fruits.pop()#return only one element 
print(fruit)
fruits.clear()
print(fruits)
fruit= {"apple", "banana", "cherry"}
while fruit:
    fruits=fruit.pop()
    print(fruits)
    print(fruit) 
"""#shown empty set beacuse each pop remove until set is empty
a={1,2,3}
b={1,2,4}
print(a.issubset(b))#contain all element
print(b.issuperset(a))#check if all element are in b
print(a.isdisjoint(b))#check if no common elements """

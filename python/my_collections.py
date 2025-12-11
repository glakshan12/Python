#list
'''a=[1,2,3,4,5]
a.append(8)
print(a)

#
a=[1,2,3,4,5]
a.insert(0,11)
print(a)

#
a=[1,2,3,4,5]
a[0]=(11)
print(a)

#
a=[1,2,3,4,5]
a.pop(1)
a.pop()
print(a)'''

#
a=[1,2,3,4,5]
b=[11,21,13,14,15]
c=[6,7,8]
a.extend(b)
print(a)

'''#tuple
a=(1,2,3,4,5)
b=list(a)
print(b)

#set
a={1,2,3,4,5}
a.add(6)
a.remove(6)
a.pop()
print(a)'''

#dict
'''a={
    "name":"laksh",
    "age":20,
    "skill":"py"
    }
a["age"]=21
a["name"]="lakshan"
a["game"]="cricket"
a.update({
    "skill":"cyber"
    })
a.pop("game")
removed=a.pop("skill")
a[" "]
print(removed)
print(a)'''

#
a={
    "name":"laksh",
    "age":20,
    "skill":"py"
    }
a["age"]=21
a.clear()#del a
print(a)


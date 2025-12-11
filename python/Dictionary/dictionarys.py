my={
    "name":"Lakshan",
    "age":21,
    "role":"Python developer"
}
print(my)
print(my["name"])
print(my.get("age"))

my["city"]="erode"
my["age"]=20
print(my)
my.pop("age")
print(my)
my.popitem()
print(my)
a = {"x": 1, "y": 2}
b = {"y": 10, "z": 3}
a.update(b)
print(a)
# my.clear()
# print(my)#empty 
laks=my.copy()
print(laks)

#dict.formkeys
mydict=["1","2","3"]
# d=dict.fromkeys(mydict,"0")
# print(d)
d=dict.fromkeys(mydict)
print(d)
d=dict.fromkeys(["a","b"],"unknown")
print(d)
mydict=["1","2","3"]
d=dict.fromkeys(mydict,[])
print(d)
d["a"]="lakshan"#both keys use same list memory
print(d)#prefernce so same output for d["2"].append("lakshan")

#nedted dictionary
students = {
    "s1": {"name": "Lakshan", "age": 21},
    "s2": {"name": "laksh", "age": 20}
}
print(students["s1"])
#sorted dictionary

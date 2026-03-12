""" import tkinter as tk

# 1. Create the main application window
root = tk.Tk()
root.title("My First GUI App")  # Set the window title

# 2. Add a widget (a Label)
label = tk.Label(root, text="Hello, world!")
label.pack()
label=tk.Label(root,text="LAKSHAN.G")
label.pack()  # Use a geometry manager to place the widget

# 3. Start the event loop
root.mainloop() """

""" dict1={'name':'Lakshan','age':20,'desigination':'software developer'}
print(dict1)
dict2=dict({'name':'Lakshan','age':20,'desigination':'software developer'})
print(dict2)
dict1['name']='Laksh'
print(dict1) """

marks={
    'a':10,
    'b':20,
}
marks["c"]=30
print(marks)#before update
marks['a']=100
print(marks)#after update
marks["math", "science"]=80,90
print(marks)
if ('math','science') in marks:
    print("yes")
for key in marks:
    print(key)
for value in marks.values():
    print(value)

student={"name":"laks","age":20}
if "mark" in student:
    print("marks is exist")
else:
    student["mark"]=50
print(student)
print(student.get("age"))
d={}
if "x" not in d:
    student["x"]=0
print(student)
print(d)

#frequency of numbers
nums=[1,2,2,3,1]
f={}
for i in nums:
    if i in f:
        f[i]=f[i]+1
    else:
        f[i]=1
print(f)

#count character frequency
s="banana"
c={}
for char in s:
    if char in c:
        c[char]=c[char]+1
    else:
        c[char]=1
print(c)

s="lakshan"
l={}
for char in s:
    #get method 
    #if key exist means it return key+1
    #else it return default values+1
    l[char]=l.get(char,0)+1
print(l)

s="code code learn python learn code"
d={}
for word in s:
    if word in d:
        d[word]=d[word]+1
    else:
        d[word]=1
print(d)
    
""" nums = [4, 3, 2, 7, 8, 2, 3, 1]
d={}
f={}
for i  in nums:
    if i not in d:
        d[i]=d[i]
    else: """

s="success"
d={}
for ch in s:
    if ch in d:
        d[ch]=d[ch]+1
    else:
        d[ch]=1
print(d)
maxcount=0
maxchar={}
for ch,count in d.items():
    if count>maxcount:
        maxcount=count
        maxchar=ch
print(maxchar)

#first non repeating characters
s="swiss"
d={}
for ch in s:
    if ch in d:
        d[ch]=d[ch]+1
    else:
        d[ch]=1
low=1
lowchar={}
for ch,count in d.items():
    if count<=low:
        low=count
        lowchar=ch
        break
print(lowchar)

#first non repeatting characters
s="swiss"
d={}
for ch in s:
    if ch in d:
        d[ch]=d[ch]+1
    else:
        d[ch]=1
for ch in s:
    if d[ch]==1:
        print(ch)
        break

#print only even value
nums={"a":15,"b":10,"c":20,"d":7}
for key,value in nums.items():
    if value %2==0:
        print(value)

#print value greater than k
nums={"a":15,"b":10,"c":20,"d":7}
k=10
for key,value in nums.items():
    if value>k:
        print(key)

nums={"a":1,"b":2,"c":3}
reverse={}
for key,value in nums.items():
    reverse[value]=key
print(reverse)

#in dictionary if same is exist again means then the it overwrite the key 
nums = {"x": 5, "y": 5, "z": 10}
inv={}
for key,value in nums.items():
    inv[value]=key
print(inv)

#add the same key value in d1 and d2
d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"b": 5, "c": 15, "d": 40}
#
res={}
res.update(d1)
for key,value in d2.items():
    if key in res:
        res[key]= res[key]+value
    else:
        res[key]=value  
print(res)


marks={"maths":60,"english":75,"biology":85,"science":76}
maxmarks=0
maxch={}
for key,value in marks.items():
    if value>maxmarks:
        maxmarks=value
        maxch=key
print(maxch)

#distinct elements count
arr=[1,2,2,3,4,4,4]
dis={}                
for i in arr:
    dis[i]=dis.get(i,0)+1
print(len(dis))
f=[]
for i in arr:
    if i in f:
        del i
    else:
        f.append(i)
print(f)
print(len(f))

arr1=[1,2,3,4]
arr2=[1,2,3,4]
f={}
f1={}
for i in arr1:
    f[i]=f.get(i,0)+1
for i in arr2:
    f1[i]=f1.get(i,0)+1
print(f)
print(f1)
if f==f1 and len(f)==len(f1):
    print("true")
else:
    print("false")

#print duplicate elements
arr=[2,3,1,2,3]
f={}
found=False
for i in arr:
    f[i]=f.get(i,0)+1
for key,value in f.items():
    if value>1:
        print(key)
        found=True
if not found:
    print(-1)

#non repeat characters
s="swiss"
f={}
for i in s:
    f[i]=f.get(i,0)+1
print(f)
found=False
for ch,count in f.items():
    if f[ch]==1:
        print(ch)
        found=True
        break
if not found:
    print("false")

# repeating most number frequency
s=[3,2,2,3]
f={}
for i in s:
    f[i]=f.get(i,0)+1
print(f)
maxvalue=0
minchar={}
for key,value in f.items():
    if value>maxvalue:
        maxvalue=value
        minchar=key
print(minchar)

#first repeat number 
arr=[10,5,3,4,3,5,6]
f={}
for i in arr:
    f[i]=f.get(i,0)+1
found=False
for ch,count in f.items():
    if count>1:
        print(ch)
        found=True
        break
if not found:
    print(-1)     

arr=[1,2,3,1,2,4]
f={}
for i in arr:
    f[i]=f.get(i,0)+1
print(f)
for key,count in f.items():
    if count>1:
        for _ in range(count):
          print(key,end=" ")

a=5
b=3
print(a&b)


a=5
b=3
print(a|b)

a=5;b=3
print(a^b)

a=5
print(~a)

a=5
b=3
print(a<<1)
print(b>>1)

n=5
if n&1 % 2==0:
    print("even")
else:
    print("odd")

a=5
b=3
a=a^b
b=a^b
a=a^b
print(a,b)

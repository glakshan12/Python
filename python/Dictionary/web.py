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
        c[char]=c.get(char,0)+1
print(char,c)

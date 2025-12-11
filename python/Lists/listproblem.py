'''marks = [45, 78, 89, 34, 56, 99, 12, 67, 88, 100]
mark=["fail" if i<40 else i for i in marks]
print(mark) 
marks.append(85)
print(marks)
mark.pop(6)
print(marks)
bonus=['pass' if i>50 else i for i in marks]
print(bonus)
fail=["fail" if i<=50 else i for i in marks]
print(fail)
pf=['pass' if i>50 else fail for i in marks]
print(pf)


marks = [45, 78, 89, 34, 56, 99, 12, 67, 88, 100]

grades=[
        "A"if m>90 else
        "B"if m>80 else
        "C"if m>70 else
        "Fail"
        for m in marks
    ]
print(grades)'''

""" cart = ["apple", "banana", "milk", "bread", "chocolate", "eggs", "chips", "juice"]
print(cart[0])
print(cart[-1])
cart.append("coffee")
print(cart)
cart.insert(0,"butter")
print(cart)
cart.pop(6)
print(cart)
cart[2]="almond milk"
print(cart)
print([items.upper() for items in cart])
print([word for word in cart if word.startswith("b")]) """
cart = ["apple", "banana", "milk", "bread", "chocolate", "eggs", "chips", "juice"]
words=[]
for word in cart:
    length=len(word)
    mid=length//2
    if(length//2==0):
        middle=word[mid-1:mid+1]
    else:
        middle=word[mid]
    words.append(middle)
print(words)

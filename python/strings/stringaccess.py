'''strip
a="***welcome to python***"
print(a.strip("***"))

#strip
text="###***  welcome to  python!   ***###"
clear=(text.strip("#*"))
final=(clear.strip())
print(final)

#replace
text = "I like Java. Java is powerful. Java is popular. But I want Python instead of Java."
print(text.replace("Java","Python"))'''

#fstrings
name="Laksh"
age=25
x=12
y=8
pi=23.1457896325
num=123654789
zeros=45
p=0.8456
print(f"My name is {name} and I am {age}")
print(f"{x=}{y=}")
print(f"{pi:.2f} {pi:.4f}")
print(f"{name:^10}")
print(f"{name:<10}")
print(f"{name:>10}")
print(f"{num:,}")
print(f"{zeros:05d}")
print(f"hexadecimal:{zeros:x},binary:{zeros:b},octal:{zeros:o}")
print(f"{zeros:.2%}")
print(f"{name.upper()},{name.lower()},{name.title()},{name.swapcase()}")
"""text="  hello world   "
print(text.strip())
print(text.lstrip())
print(text.rstrip())
name="Laksh"
print(name.upper())
print(name.lower())
filename="laksh.pdf"
print(filename.endswith(".pdf"))
print(filename.startswith("lak"))
fruit="apple,banana,orange"
print(fruit.split(","))
txt=['red', 'blue', 'green']
print("|".join(txt))
re="I like cricket"
print(re.replace("cricket","CRICKET"))
a="python is easy, python is powerful"
print(a.find("python"))
print(a.count("python"))
print(f"My name is {name} and i am 20 years old")"""    

#challange from chatgpt
""" raw_text =  "   Python is powerful, PYTHON is easy, I like python!!!    "
print(raw_text.strip())
print(raw_text.lower())
print(raw_text.count("python"))
print(raw_text.replace("!!!","..."))
print(raw_text.startswith("Python"))
print(raw_text.endswith("."))
words=raw_text.split()
print(words)
print("|".join(words))
cleaned="python"
print(f"the cleaned text is {cleaned}")
print(f"the word,'python' appears {cleaned.count("python")} times")
print(f"the word,\"python\"appears {cleaned.count("python")} times")
print(raw_text.isalnum())
print(raw_text.capitalize())
print(raw_text.title())
#print(raw_text.index(0)) 
print(raw_text.isdigit())
print(raw_text.isalpha()) 
print(raw_text.swapcase())
clean=raw_text.strip()
print(raw_text.center(65))
print(raw_text.zfill(3)) """
heading=["name","role","salary"]
data=[["lakshan","developer","60000"],
      ["laksh","developer","50000"]
      ]
print(heading[0].ljust(10)+heading[1].center(20)+heading[2].rjust(15))
print("_"*45)
for row in data:
    print(row[0].ljust(10)+row[1].center(20)+row[2].rjust(15))


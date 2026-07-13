import sys
import math
from decimal import Decimal

print("--- 1. INTEGER INTERNING (The Memory Trick) ---")
# Python pre-allocates small integers (-5 to 256)
users_a = 250
users_b = 250
# 'is' checks if they share the exact same memory address
print(f"Do 250 and 250 share memory? {users_a is users_b}")

# Larger integers get their own fresh memory addresses
revenue_a = 10000
revenue_b = 10000
print(f"Do 10000 and 10000 share memory? {revenue_a is revenue_b}")


print("\n--- 2. ARBITRARY PRECISION (Infinite Size) ---")
# AI models require massive parameter counts. Let's make a huge number.
nexura_parameters = 10 ** 150 # 10 to the power of 150
print(f"Memory size of normal int (10): {sys.getsizeof(10)} bytes")
print(f"Memory size of huge int: {sys.getsizeof(nexura_parameters)} bytes")
print("Notice how it didn't crash? The memory footprint just grew dynamically.")


print("\n--- 3. THE FLOAT TRAP (Binary Precision) ---")
# Calculating cloud server costs
server_cost_1 = 0.1
server_cost_2 = 0.2
actual_total = server_cost_1 + server_cost_2

print(f"Computer's math: 0.1 + 0.2 = {actual_total}")
print(f"Does 0.3000... == 0.3? {actual_total == 0.3}")
print(f"The correct way to check (math.isclose): {math.isclose(actual_total, 0.3)}")


print("\n--- 4. THE FIX: USING DECIMAL FOR MONEY ---")
# When accuracy is non-negotiable, use Decimal
exact_cost_1 = Decimal('0.1')  # Note: Pass it as a string!
exact_cost_2 = Decimal('0.2')
print(f"Decimal math: 0.1 + 0.2 = {exact_cost_1 + exact_cost_2}")


print("\n--- 5. DIVISION & BOOLEAN TRUTH ---")
total_compute_hours = 100
task_duration = 3

# Floor division (//) to find how many FULL tasks we can run
full_tasks = total_compute_hours // task_duration
print(f"Full tasks we can complete: {full_tasks}")

# Modulo (%) to find leftover hours
leftover = total_compute_hours % task_duration

# Any number other than 0 is inherently 'True'
if bool(leftover):
    print(f"We have {leftover} hour(s) left over. (Evaluated as True)")


name="lakshan"
age=20
print (f"My name is {name} and i am {age} years old")

a=10
b=20
a,b=b,a
print(a,b)

raw_invoice="TXN-994-PAID-3000"
#print(raw_invoice[-4:])
amt_string=raw_invoice[-4:]
amount=int(amt_string)
reverse=amount//2
final_message="saved :" +str(reverse)
print(final_message)

""" raw_data = "Agent_Alpha|Hours:040|Rate:075.50"
hours=raw_data[18:21]
rate=raw_data[-5:]
h=int(hours)
r=int(rate)
total=h+r
expense=reverse-total
print(expense)
if total>=3000:
    print(f"Success! Total revenue is {total}, which covers the 3000 expense, with {expense} remaining.") """

num=123
reve=0
while num>0:
    d=num%10
    reve=reve*10+d
    num=num//10
print(reve)

a=10
b=20
a,b=b,a
print(a,b)

name="Lakshan"
age=21
print(f"I'm {name},{age} years old")
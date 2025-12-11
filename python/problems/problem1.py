items = []   # empty list to store (name, price)

while True:
    name = input("Enter item name (or type 'done' to finish): ")
    if name.lower() == "done":
        break
    price = float(input("Enter item price: "))
    items.append((name, price))

# Print the bill
print("\n--- Shopping Bill ---")
total = 0
for name, price in items:
    print(f"{name} - ₹{price}")
    total += price

print("----------------------")
print("Total Bill: ₹", total)

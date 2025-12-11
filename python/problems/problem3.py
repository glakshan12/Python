balance=0
while True:
    bank=input("create bank account(or type 'exit'):")
    if bank.lower()=="exit":
        break
    deposit=int(input("enter your deposit money:"))
    balance+=deposit
    print(balance)
    withdraw=int(input("enter your withdraw money:"))
    balance-=withdraw
    print(balance)
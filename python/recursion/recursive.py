#printing numbers from 1 to n using recursion 
def numbers(n):
    if n==0:
        return
    numbers(n-1)#post 
    print(n)
numbers(3)
""" 
def numbers(n):
    if n==0:
        return
    print(n)#pre
    numbers(n-1)
numbers(3)

#factorial of a number
def factorial(y):
    if y==1:
        return 1
    return y*factorial(y-1)
print(factorial(5))

#fibanocci series
def fibanocci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    fibanocci(n-1)+fibanocci(n-2)
print(fibanocci(6))

#sum of digits
def sum(n):
    if n==0:
        return 0
    return (n%10) + sum(n//10)
print(sum(1234)) """





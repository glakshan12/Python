#prime
n=5
current=2
while current<=n:
    is_prime=True
    i=2
    while i<current:
        if current%i==0:
            is_prime=False
            break
        i=i+1
    if is_prime ==True:
        print(current,end=" ")
    current+=1
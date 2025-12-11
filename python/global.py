def outer():
    x=5
    def inner():
        nonlocal x
        x=10
        print(x)
    inner()
    print(x)
outer()

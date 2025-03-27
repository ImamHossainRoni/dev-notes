def outer():
    x = "Hello"

    def inner():
        nonlocal x
        x = "Hi"

    inner()
    print(x)


outer()

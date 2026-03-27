def fib_list(n):
    a = 0
    b = 1
    fib = []
    if n <= 1:
        fib.append(a)
    else:
        fib.append(a)
        fib.append(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            fib.append(b)
    return fib

print(fib_list(6))



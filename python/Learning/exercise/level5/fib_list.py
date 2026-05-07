def fib_list(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]

    a = 1
    b = 1
    fib = [a, b]

    for i in range(2, n):
        c = a + b
        a = b
        b = c
        fib.append(b)

    return fib

print(fib_list(6))

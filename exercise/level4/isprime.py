def is_prime(n):
    if n <= 1:
         return print("请输入大于一的整数")
    elif n == 2:
        return print("2是素数")
    else:
        for each in range(2, n):
            if n % each == 0:
                return print("False")
            else:
                return print("True")
        return None


is_prime(5)
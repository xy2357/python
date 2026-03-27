def is_prime(n):
    if n <= 1:
         return False
    else:
        for each in range(2, n):
            if n % each == 0:
                return False
        else:
            return True
num = int(input("请输入一个数字："))
print(is_prime(num))
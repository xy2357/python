nums = []
i = 1
positive, negative, zero = 0, 0, 0

while i <= 6:
    num = int(input(f"请输入第{i}个数字："))
    nums.append(num)
    i += 1

for each in nums:
    if each > 0:
        positive += 1
    if each < 0:
        negative += 1
    if each == 0:
        zero += 1

print(f"正数有{positive}个")
print(f"负数有{negative}个")
print(f"零有{zero}个")
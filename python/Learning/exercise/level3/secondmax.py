nums = []
i = 1
while i <= 10:
    num = int(input(f"请输入第{i}个数字："))
    nums.append(num)
    i += 1

deduplication = []
for each in nums:
    if each not in deduplication:
        deduplication.append(each)

maximum = deduplication[0]
for each in deduplication:
    if maximum < each:
        maximum = each
deduplication.remove(maximum)

maximum = deduplication[0]
for each in deduplication:
    if maximum < each:
        maximum = each
print(maximum)
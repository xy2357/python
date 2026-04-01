nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4]
counter = {}
for each in nums:
    if each in counter:
        counter[each] += 1
    else:
        counter[each] = 1
max_count = 0
max_key = ""
for key, value in counter.items():
    if value > max_count:
        max_count = value
        max_key = key

print(f"{max_key}的个数为{max_count} ")


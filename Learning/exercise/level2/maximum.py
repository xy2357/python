nums = []
i = 1
while i <= 5:
    num = int(input(f"请输入第{i}个数字："))
    nums.append(num)
    i += 1

maximum = nums[0]
for each in nums:
    if maximum < each:
        maximum = each

print(maximum)
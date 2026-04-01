nums = [3, -1, 5, -7, 0, 8, -2]
for i in range(0, len(nums)):
    if nums[i] < 0:
        nums[i] = 0
print(nums)
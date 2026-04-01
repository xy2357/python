nums = [8, 3, 5, 2, 9, 1, 8, 0]
for i in range(1, len(nums)):
    for j in range(i):
        if nums[i] < nums[j]:
            nums.insert(j, nums.pop(i))
            break

print(nums)
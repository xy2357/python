nums = [5, 3, 8, 1, 6]
inter = 0
for i in range(0, len(nums)-1):
    for j in range(0, len(nums)-i -1):
        if nums[j] > nums[j+1]:
            inter = nums[j+1]
            nums[j+1] = nums[j]
            nums[j] = inter
print(nums)


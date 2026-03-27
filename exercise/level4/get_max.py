def get_max(nums):
    max_num = nums[0]
    for i in range(0, len(nums)):
        if max_num < nums[i]:
            max_num = nums[i]
    return max_num

print(get_max([-1, -9]))
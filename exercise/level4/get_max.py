def get_max(nums):
    max_num = 0
    for i in range(0, len(nums)):
        if max_num < nums[i]:
            max_num = nums[i]
    print(max_num)

get_max([1, 2, 3, 4, 5, 6])
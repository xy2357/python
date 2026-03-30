def find_even(nums):
    even_nums = []
    for each in nums:
        if each % 2 == 0:
            even_nums.append(each)
    return  even_nums

nums = [1, 2, 3, 4, 5, 6]

print(find_even(nums))
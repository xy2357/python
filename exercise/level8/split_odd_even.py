def split_odd_even(nums):
    odd_list = []
    even_list = []
    for each in nums:
        if each % 2 == 0:
            odd_list.append(each)
        else:
            even_list.append(each)
    return even_list, odd_list

nums = [1, 2, 3, 4, 5, 6]
print(split_odd_even(nums))
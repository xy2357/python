def count_all_items(nums):
    items_dict = {}
    for each in nums:
        if each in items_dict:
            items_dict[each] += 1
        else:
            items_dict[each] = 1
    return  items_dict

print(count_all_items([1, 2, 2, 3, 1, 1]))

def count_all(nums):
    num_dict = {}
    for each in nums:
        if each in num_dict:
            num_dict[each] += 1
        else:
            num_dict[each] = 1
    return  num_dict

def most_common(nums):
    num_dict = count_all(nums)
    most_value = None
    for key, value in num_dict.items():
        if value == max(num_dict.values()):
            most_value = key
    return most_value

nums_list = [int(x) for x in input("请输入:").split(" ")]
print(most_common(nums_list))
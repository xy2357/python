def remove_duplicates(nums):
    res_list = []
    for each in nums:
        if each not in res_list:
            res_list.append(each)
    return res_list

num_list = [int(x) for x in input("请输入一串数字：").split(" ")]

print(remove_duplicates(num_list))

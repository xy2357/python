nums = [1, 2, 3, 2, 4, 5, 1, 6, 3]
find_list = []
while nums:
    a = nums.pop()
    if a in nums:
        find_list.append(a)
print(find_list)
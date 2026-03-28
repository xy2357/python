def count_item(nums, target):
    count = 0
    for each in nums:
        if each == target:
            count += 1
    return count

nums = [int(num) for num in input("请输入一组数字：").split(" ")]
target = int(input("请输入目标数字："))
print(count_item(nums, target))
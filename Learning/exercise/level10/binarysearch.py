def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

nums = [1, 2, 2, 2, 3, 4, 5]
print(binary_search(nums, 2))

def find_left(nums, target):
    left = 0
    right = len(nums) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            if nums[mid] == target:
                ans = mid
            right = mid - 1
    return ans

def find_right(nums, target):
    left = 0
    right = len(nums) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        else:
            if nums[mid] == target:
                ans = mid
            left = mid + 1
    return ans

def binary_search_all(nums, target):
    left_index = find_left(nums, target)

    if left_index == -1:
        return []

    right_index = find_right(nums, target)

    result = []
    i = left_index
    while i <= right_index:
        result.append(i)
        i += 1
    return result

print(binary_search_all(nums, 2))
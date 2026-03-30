def merge_sorted_list(list_a, list_b):
    merge_list = []
    for i in range(len(list_a)):
        merge_list.append(list_a[i])
        merge_list.append(list_b[i])
    return merge_list

a = [1, 3, 5]
b = [2, 4, 6]

print(merge_sorted_list(a, b))

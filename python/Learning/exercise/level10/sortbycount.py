def count_by_key(items, key_name):
    count_dict = {}
    for each in items:
        for key in each.keys():
            if key == key_name:
                if each[key] in count_dict:
                    count_dict[each[key]] += 1
                else:
                    count_dict[each[key]] = 1

    return count_dict

def sort_count_result(count_dict):
    count_list = []
    for key in count_dict:
        count_list.append((key, count_dict[key]))

    i = 0
    while i < len(count_list) - 1:
        j = 0
        while j < len(count_list) - 1 - i:
            if count_list[j][1] < count_list[j + 1][1]:
                temp = count_list[j]
                count_list[j] = count_list[j + 1]
                count_list[j + 1] = temp
            j += 1
        i += 1
    return count_list

logs = [
    {"user": "A", "action": "login"},
    {"user": "B", "action": "login"},
    {"user": "A", "action": "view"},
    {"user": "A", "action": "logout"},
    {"user": "B", "action": "view"}
]

print(sort_count_result(count_by_key(logs, "action")))
def filter_items(items, key_name, min_value):
    filter_list = []
    for each in items:
        if each[key_name] >= min_value:
            filter_list.append(each)
    return filter_list

students = [
    {"name": "小明", "score": 85},
    {"name": "小红", "score": 92},
    {"name": "小刚", "score": 78}
]

print(filter_items(students, "score", 80))
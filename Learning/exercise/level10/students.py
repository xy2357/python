students = [
    {"name": "小明", "score": 85, "class": "一班"},
    {"name": "小红", "score": 92, "class": "一班"},
    {"name": "小刚", "score": 78, "class": "二班"},
    {"name": "小美", "score": 96, "class": "二班"},
    {"name": "小华", "score": 88, "class": "一班"}
]

total_score = 0
max_student = ''
max_score = 0
min_student = ''
min_score = 100
class_dict = {}

for student in students:
    total_score += student['score']

    if student['score'] > max_score:
        max_student = student['name']
        max_score = student['score']

    if student['score'] < min_score:
        min_student = student['name']
        min_score = student['score']

    if student['class'] in class_dict:
        class_dict[student['class']]['num'] += 1
        class_dict[student['class']]['total_score'] += student['score']
    else:
        class_dict[student['class']] = {'num': 1, 'total_score': student['score']}

for each in class_dict:
    print(f"{each}有{class_dict[each]['num']}人")
    print(f"{each}的平均分为{class_dict[each]['total_score'] / class_dict[each]['num']}")
print(f"最高分为{max_student}")
print(f"最高分为{min_student}")
average_score = total_score / len(students)
print(average_score)
# print(class_dict)
for student in students:
    if student['score'] > average_score:
        print(f"{student['name']}分数高于平均分")
import csv

csv_list = []
class_dict = {}
total = 0
max_student = ''
max_score = 0

with open('scores.csv', 'r', encoding='utf-8', newline='') as file:
    data = csv.reader(file)

    for i, row in enumerate(data):
        row_dict = {}
        if i == 0:
            key_name = row
        else:
            for j in range(len(row)):
                row_dict[key_name[j]] = row[j]
            csv_list.append(row_dict)
    # print(csv_list)

for student in csv_list:
    student_score =  int(student['score'])
    total += student_score
    if student_score > max_score:
        max_score = student_score
        max_student = student['name']

print(f"全体平均分为：{total/len(csv_list)}")
print(f"最高分学生为{max_student},分数为{max_score}")

for each in csv_list:
    if each['class'] not in class_dict:
        class_dict[each['class']] = [{'name':each['name'], 'score':each['score']}]
    else:
        class_dict[each['class']].append({'name':each['name'], 'score':each['score']})

for cls in class_dict:
    total_class = 0
    for cls_student in class_dict[cls]:
        total_class += int(cls_student['score'])
    print(f"{cls}的人数为{len(class_dict[cls])},平均分为{total_class/len(class_dict[cls])}")
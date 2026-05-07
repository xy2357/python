students = {
    "小明": {"age": 18, "score": 90},
    "小红": {"age": 17, "score": 95},
    "小刚": {"age": 18, "score": 85}
}
total_age = 0
total_score = 0
max_student = ""
max_score = 0
min_student = ""
min_score = 100


for name,student in students.items():
    total_age += students[name]['age']
    total_score += students[name]['score']
    if students[name]['score'] > max_score:
        max_score = students[name]['score']
        max_student = name
    if students[name]['score'] < min_score:
        min_score = students[name]['score']
        min_student = name

average_age = total_age / len(students)
average_score = total_score / len(students)

print(f"平均年龄是：{average_age}")
print(f"平均分是：{average_score}")
print(f"{max_student}为最高分")
print(f"{min_student}为最低分")
students = {}
name = input("请输入名字：")
if name != "q":
    score = int(input("请输入成绩："))
while name != "q":
    students[name] = score
    name = input("请输入名字：")
    if name != "q":
        score = int(input("请输入成绩："))
    else:
        break
total, average = 0, 0
for key, value in students.items():
    total += value
if len(students) != 0:
    average = total / len(students)
    print(students)
    print(f"平均分为:{average}")
else:
    print("查无学生")

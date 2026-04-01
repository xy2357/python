students = {}
student = {}
while True:
    print("1.录入学生\n2.查询学生\n3.退出")
    menu = input("请输入操作：")
    if menu == "1":
        name = input("请输入姓名：")
        age = int(input("请输入年龄："))
        score = int(input("请输入分数："))
        students[name] = {"age":age, "score":score}
        print(students)

    elif menu == "2":
        name = input("请输入姓名：")
        if name in students:
            print(f"{name}的年龄是{students[name]['age']},分数是{students[name]['score']}")
        else:
            print("查无此人")

    elif menu == "3":
        break
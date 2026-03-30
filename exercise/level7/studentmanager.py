students = []
while True:
    print("1.查看所有学生\n2.添加学生\n3.查询学生\n4.删除学生\n5.修改学生成绩\n6.退出")
    index = input("请输入操作：")

    if index == "1":
        if len(students) != 0:
            for each in students:
                print(f"{each["name"]}的年龄为{each['age']},分数为{each['score']}")
        else:
            print("没有学生")

    if index == "2":
        name = input("请输入学生姓名：")
        age = int(input("请输入年龄："))
        score = int(input("请输入分数："))
        students.append({"name":name, "age":age, "score":score})

    if index == "3":
        name = input("请输入学生姓名：")
        if len(students) != 0:
            for each in students:
                if name in each['name']:
                    print(f"{each['name']}的年龄为{each['age']}，分数为{each['score']}")
                else:
                    print("查无此人")

    if index == "4":
        name = input("请输入学生姓名：")
        if len(students) != 0:
            for each in students:
                if name in each['name']:
                    students.remove(each)
                else:
                    print("查无此人")

    if index == "5":
        name = input("请输入学生姓名：")
        if len(students) != 0:
            for each in students:
                score = int(input("请输入分数："))
                if name in each['name']:
                    each['score'] = score
                else:
                    print("查无此人")

    if index == "6":
        break

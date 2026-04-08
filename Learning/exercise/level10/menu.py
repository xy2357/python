students = [{"name": "小明", "age": 18, "score": 90}]
while True:
    found = False
    total_score = 0
    average_score = 0
    temp = {}
    print("1.查看全部数据\n2.添加数据\n3.查询\n4.修改\n5.删除\n6.统计\n7.排序\n8.退出")
    index = input("请输入操作：")

    if index == '1':
        if len(students) != 0:
            for each in students:
                print(f"{each['name']}的年龄是{each['age']},分数为{each['score']}")
        else:
            print("数据为空！")

    elif index == '2':
        name = input("请输入姓名：")
        age = int(input("请输入年龄："))
        score = int(input("请输入分数："))
        students.append({"name":name, "age":age, "score":score})

    elif index == '3':
        if len(students) != 0:
            name = input("请输入姓名：")
            for each in students:
                if name == each['name']:
                    print(f"{name}的年龄是{each['age']},分数为{each['score']}")
                    found = True
                    break
            if not found:
                print(f"{name}不存在！")

    elif index == '4':
        if len(students) != 0:
            name = input("请输入姓名：")
            for each in students:
                if name == each['name']:
                    score = int(input("请输入分数："))
                    each['score'] = score
                    found = True
                    break
            if not found:
                print(f"{name}不存在！")

    elif index == '5':
        if len(students) != 0:
            name = input("请输入姓名：")
            for each in students:
                if name == each['name']:
                    students.remove(each)
                    found = True
                    break
            if not found:
                print(f"{name}不存在！")

    elif index == '6':
        if len(students) != 0:
            for each in students:
                total_score += each['score']
            average_score = total_score / len(students)
            print(f"平均分为{average_score}")

    elif index == '7':
        for i in range(len(students) - 1):
            for j in range(len(students) - i - 1):
                if students[j]['score'] < students[j+1]['score']:
                    temp = students[j+1]
                    students[j+1] = students[j]
                    students[j] = temp

        for each in students:
            print(f"{each['name']}的年龄是{each['age']},分数为{each['score']}")

    elif index == '8':
        break



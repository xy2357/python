# students = {}
# menu = int(input("1.查看所有学生\n2.添加学生\n3.查询学生成绩\n4.修改学生成绩\n5.退出\n选择操作:"))
# while menu in [1, 2, 3, 4, 5]:
#     if menu == 1:
#         print(students)
#         menu = int(input("1.查看所有学生\n2.添加学生\n3.查询学生成绩\n4.修改学生成绩\n5.退出\n选择操作:"))
#     if menu == 2:
#         name = input("请输入姓名：")
#         score = input("请输入成绩：")
#         students[name] = score
#         menu = int(input("1.查看所有学生\n2.添加学生\n3.查询学生成绩\n4.修改学生成绩\n5.退出\n选择操作:"))
#     if menu == 3:
#         name = input("请输入姓名：")
#         if name in students:
#             print(students[name])
#             menu = int(input("1.查看所有学生\n2.添加学生\n3.查询学生成绩\n4.修改学生成绩\n5.退出\n选择操作:"))
#         else:
#             print("查无此人")
#             menu = int(input("1.查看所有学生\n2.添加学生\n3.查询学生成绩\n4.修改学生成绩\n5.退出\n选择操作:"))
#     if menu == 4:
#         name = input("请输入姓名：")
#         if name in students:
#             score = input("请输入成绩：")
#             students[name] = score
#             menu = int(input("1.查看所有学生\n2.添加学生\n3.查询学生成绩\n4.修改学生成绩\n5.退出\n选择操作:"))
#         else:
#             print("查无此人")
#             menu = int(input("1.查看所有学生\n2.添加学生\n3.查询学生成绩\n4.修改学生成绩\n5.退出\n选择操作:"))
#     if menu == 5:
#         break


students = {}

while True:
    print("\n1.查看所有学生")
    print("2.添加学生")
    print("3.查询学生成绩")
    print("4.修改学生成绩")
    print("5.退出")

    menu = input("请选项操作：")

    if menu == "1":
        if students:
            for name, score in students.items():
                print(f"{name}: {score}")
        else:
            print("当前没有学生成绩！")

    elif menu == "2":
        name = input("请输入名字：")
        score = int(input("请输入成绩："))
        students[name] = score
        print("添加成功！")

    elif menu == "3":
        name = input("请输入名字：")
        if name in students:
            print(f"{name}的成绩是：{students[name]}")
        else:
            print("查无此人")

    elif menu == "4":
        name = input("请输入姓名：")
        if name in students:
            score = int(input("请输入新成绩："))
            students[name] = score
            print("修改成功")
        else:
            print("查无此人")

    elif menu == "5":
        print("程序结束")
        break

    else:
        print("无效选项，请重新输入")
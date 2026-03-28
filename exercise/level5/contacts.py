contacts = {}
while True:
    print("1.查看所有联系人\n2.添加联系人\n3.查询联系人\n4.删除联系人\n5.退出")
    menu = input("请输入操作：")
    if menu == "1":
        if len(contacts) != 0:
            for name, num in contacts.items():
                print(f"{name}的手机号是{num}")
        else:
            print("通讯录为空")

    if menu == "2":
        name = input("请输入名字：")
        num = int(input("请输入手机号："))
        contacts[name] = num

    if menu == "3":
        name = input("请输入名字：")
        if name in contacts:
            print(f"{name}的手机号是：{contacts[name]}")
        else:
            print("查无此人")

    if menu == "4":
        name = input("请输入名字：")
        if name in contacts:
            del contacts[name]
        else:
            print("查无此人")

    if menu == "5":
        break
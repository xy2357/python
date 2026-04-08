import json
from pathlib import Path

# contacts = {}
# with open('contacts.json', 'w') as file:
#     json.dump(contacts, file)

while True:
    print("1.查看所有联系人\n2.添加联系人\n3.查询联系人\n4.修改联系人电话\n5.删除联系人\n6.退出程序")
    index = input("请输入操作：")

    if index == '1':
        if Path('contacts.json').exists():
            with open('contacts.json', 'r') as file:
                contacts = json.load(file)
                if len(contacts) != 0:
                    for contact, tel in contacts.items():
                        print(f"{contact}的电话号码是{tel}")
                else:
                    print("联系人为空！")
        else:
            print("没有找到文件！")

    elif index == '2':
        if Path('contacts.json').exists():
            with open('contacts.json', 'r') as file:
                contacts = json.load(file)
                name = input("请输入姓名：")
                tel = input("请输入电话号码：")
                contacts[name] = tel
                # print(contacts)

    elif index == '3':
        if Path('contacts.json').exists():
            with open('contacts.json', 'r') as file:
                contacts = json.load(file)
                name = input("请输入姓名：")
                for contact, tel in contacts.items():
                    if name == contact:
                        print(f"{contact}的电话号码是{tel}")

    elif index == '4':
        if Path('contacts.json').exists():
            with open('contacts.json', 'r') as file:
                contacts = json.load(file)
                name = input("请输入姓名：")
                for contact, tel in contacts.items():
                    if name == contact:
                        tel = input("请输入新的电话号码")
                        contacts[name] = tel

    elif index == '5':
        if Path('contacts.json').exists():
            with open('contacts.json', 'r') as file:
                contacts = json.load(file)
                name = input("请输入姓名：")
                if name in contacts:
                    del contacts[name]

    elif index == '6':
        with open('contacts.json', 'w') as file:
            json.dump(contacts, file)
        break

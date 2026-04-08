import json
from pathlib import Path

def save_contacts(contacts):
    with open('contacts.json', 'w', encoding="utf-8") as file:
        json.dump(contacts, file, ensure_ascii=False)

def open_contacts():
    with open('contacts.json', 'r', encoding="utf-8") as file:
        contacts = json.load(file)

    return contacts

try:
    if Path('contacts.json').exists():

        contacts = open_contacts()

        if isinstance(contacts,dict):
            pass

        else:
            contacts = {}

            save_contacts(contacts)
    else:
        contacts = {}

        save_contacts(contacts)
        contacts = open_contacts()

except json.JSONDecodeError as e:
    print("文件已损坏！")

    contacts = {}

    save_contacts(contacts)
    contacts = open_contacts()

while True:

    print("1.查看所有联系人\n2.添加联系人\n3.查询联系人\n4.修改联系人电话\n5.删除联系人\n6.退出程序")
    index = input("请输入操作：")

    if index == '1':
        if len(contacts) != 0:
            for contact, tel in contacts.items():
                print(f"{contact}的电话号码是{tel}")
        else:
            print("联系人为空！")

    elif index == '2':
        name = input("请输入姓名：")
        while name in contacts:
            confirm = input("联系人已存在，是否重新输入姓名:y/n")
            if confirm == 'y':
                name = input("请输入姓名：")
                continue
            else:
                tel = input("请输入电话号码：")
                contacts[name] = tel
                save_contacts(contacts)
                break
        else:
            tel = input("请输入电话号码：")
            contacts[name] = tel
            save_contacts(contacts)

    elif index == '3':
        name = input("请输入姓名：")
        if name in contacts:
            print(f"{name}的电话号码是{contacts[name]}")
        else:
            print("查无此人！")

    elif index == '4':
        name = input("请输入姓名：")
        if name in contacts:
            tel = input("请输入新的电话号码")
            contacts[name] = tel
            save_contacts(contacts)
        else:
            print("查无此人！")

    elif index == '5':
        name = input("请输入姓名：")
        if name in contacts:
            del contacts[name]
            save_contacts(contacts)
        else:
            print("查无此人！")

    elif index == '6':
        save_contacts(contacts)
        break

    else:
        print("请输入有效操作！")
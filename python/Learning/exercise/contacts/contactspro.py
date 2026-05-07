import json
from pathlib import Path

FILE_PATH = Path("contacts.json")


def load_contacts():
    if not FILE_PATH.exists():
        return {}

    try:
        with FILE_PATH.open("r", encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, dict):
            return data
        return {}
    except json.JSONDecodeError:
        print("contacts.json 文件内容损坏，已重置为空通讯录。")
        return {}


def save_contacts(contacts):
    with FILE_PATH.open("w", encoding="utf-8") as file:
        json.dump(contacts, file, ensure_ascii=False, indent=2)


def show_all_contacts(contacts):
    if not contacts:
        print("联系人为空！")
        return

    for name, phone in contacts.items():
        print(f"{name} 的电话号码是 {phone}")


def add_contact(contacts):
    name = input("请输入姓名：").strip()
    if not name:
        print("姓名不能为空！")
        return

    if name in contacts:
        choice = input("联系人已存在，是否覆盖旧号码？(y/n)：").strip().lower()
        if choice != "y":
            print("已取消添加。")
            return

    phone = input("请输入电话号码：").strip()
    if not phone:
        print("电话号码不能为空！")
        return

    contacts[name] = phone
    save_contacts(contacts)
    print("保存成功。")


def find_contact(contacts):
    name = input("请输入姓名：").strip()
    if name in contacts:
        print(f"{name} 的电话号码是 {contacts[name]}")
    else:
        print("查无此人！")


def update_contact(contacts):
    name = input("请输入姓名：").strip()
    if name not in contacts:
        print("查无此人！")
        return

    phone = input("请输入新的电话号码：").strip()
    if not phone:
        print("电话号码不能为空！")
        return

    contacts[name] = phone
    save_contacts(contacts)
    print("修改成功。")


def delete_contact(contacts):
    name = input("请输入姓名：").strip()
    if name not in contacts:
        print("查无此人！")
        return

    del contacts[name]
    save_contacts(contacts)
    print("删除成功。")


def main():
    contacts = load_contacts()
    save_contacts(contacts)

    while True:
        print("\n1.查看所有联系人")
        print("2.添加联系人")
        print("3.查询联系人")
        print("4.修改联系人电话")
        print("5.删除联系人")
        print("6.退出程序")

        choice = input("请输入操作：").strip()

        if choice == "1":
            show_all_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            find_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("程序已退出。")
            break
        else:
            print("请输入有效操作！")


if __name__ == "__main__":
    main()
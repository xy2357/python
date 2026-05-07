import json
from pathlib import Path

FILE_PATH = Path("todo.json")


def load_todos():
    if not FILE_PATH.exists():
        return []

    try:
        with FILE_PATH.open("r", encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, list):
            return data
        print("文件格式错误，已重置为空数据。")
        return []
    except json.JSONDecodeError:
        print("文件内容损坏，已重置为空数据。")
        return []


def save_todos(todos):
    with FILE_PATH.open("w", encoding="utf-8") as file:
        json.dump(todos, file, ensure_ascii=False, indent=2)


def input_index(prompt, todos):
    while True:
        text = input(prompt).strip()
        try:
            num = int(text)
            if num < 1 or num > len(todos):
                print("序号越界！")
                continue
            return num - 1
        except ValueError:
            print("请输入整数！")


def show_all_todos(todos):
    if not todos:
        print("暂无数据！")
        return

    for i, todo in enumerate(todos, start=1):
        status = "已完成" if todo["done"] else "未完成"
        print(f"{i}. {todo['title']} - {status}")


def show_pending_todos(todos):
    if not todos:
        print("暂无数据！")
        return

    found = False
    for i, todo in enumerate(todos, start=1):
        if not todo["done"]:
            print(f"{i}. {todo['title']} - 未完成")
            found = True

    if not found:
        print("暂无未完成事项！")


def add_todo(todos):
    title = input("请输入事项名称：").strip()
    if not title:
        print("事项名称不能为空！")
        return

    for todo in todos:
        if todo["title"] == title:
            print("事项已存在！")
            return

    todos.append({"title": title, "done": False})
    save_todos(todos)
    print("添加成功。")


def delete_todo(todos):
    if not todos:
        print("暂无数据！")
        return

    show_all_todos(todos)
    index = input_index("请输入要删除的事项序号：", todos)
    deleted_title = todos[index]["title"]
    del todos[index]
    save_todos(todos)
    print(f"已删除：{deleted_title}")


def complete_todo(todos):
    if not todos:
        print("暂无数据！")
        return

    show_all_todos(todos)
    index = input_index("请输入要标记完成的事项序号：", todos)

    if todos[index]["done"]:
        print("该事项已经是已完成状态。")
        return

    todos[index]["done"] = True
    save_todos(todos)
    print("标记完成。")


def main():
    todos = load_todos()
    save_todos(todos)

    while True:
        print("\n1. 查看全部事项")
        print("2. 查看未完成事项")
        print("3. 添加事项")
        print("4. 删除事项")
        print("5. 标记事项完成")
        print("6. 退出")

        choice = input("请输入操作：").strip()

        if choice == "1":
            show_all_todos(todos)
        elif choice == "2":
            show_pending_todos(todos)
        elif choice == "3":
            add_todo(todos)
        elif choice == "4":
            delete_todo(todos)
        elif choice == "5":
            complete_todo(todos)
        elif choice == "6":
            save_todos(todos)
            print("程序已退出。")
            break
        else:
            print("请输入有效操作！")


if __name__ == "__main__":
    main()
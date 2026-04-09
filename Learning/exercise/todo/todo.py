import json
from pathlib import Path

FILE_PATH = Path("todo.json")

def load_todo():
    if not FILE_PATH.exists():
        return []

    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            data = json.load(file)
        if isinstance(data, list):
            return data
        print("文件格式错误！")
        return []
    except json.JSONDecodeError:
        print("文件已损坏！")
        return []

def save_todo(todo):
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(todo, file, ensure_ascii=False, indent=2)

def input_int(prompt, todo):
    """安全读取整数。"""
    while True:
        text = input(prompt).strip()
        try:
            num = int(text)
            if num < 1 or num > len(todo):
                print("序号越界！")
                continue
            return num - 1
        except ValueError:
            print("请输入整数！")

def show_all_event(todo):
    if len(todo) == 0:
        print("暂无数据！")
        return

    for i, event in enumerate(todo,start=1):
        status = '已完成' if event['done'] else '未完成'
        print(f"{i}. {event['title']} - {status}")

def show_not_done(todo):
    found = False
    if len(todo) == 0:
        print("暂无数据！")
        return

    for i, event in enumerate(todo, start=1):
        if not event['done']:
            print(f"{i}. {event['title']}")
            found = True
    if not found:
        print("暂无未完成事项！")

def add_event(todo):
    found = False
    event_title = input("请输入名称：").strip()
    if not event_title:
        print("事项名称不能为空！")
        return

    for event in todo:
        if event_title == event['title']:
            print("事项已存在！")
            found = True
            break
    if not found:
        todo.append({'title':event_title, 'done':False})
        save_todo(todo)

def delete_event(todo):
    if len(todo) == 0:
        print("暂无数据！")
        return

    event_index = input_int("请输入事项序号：", todo)
    del todo[event_index]
    save_todo(todo)

def done_event(todo):
    if len(todo) == 0:
        print("暂无数据！")
        return

    event_index = input_int("请输入事项序号：", todo)
    todo[event_index]['done'] = True
    save_todo(todo)

def main():

    todo = load_todo()
    save_todo(todo)

    while True:
        print("\n1.查看全部事项")
        print("2.查看未完成事项")
        print("3.添加事项")
        print("4.删除事项")
        print("5.事项标记完成")
        print("6.退出")

        choice = input("请输入操作：")

        if choice == "1":
            show_all_event(todo)
        elif choice == "2":
            show_not_done(todo)
        elif choice == "3":
            add_event(todo)
        elif choice == "4":
            delete_event(todo)
        elif choice == "5":
            done_event(todo)
        elif choice == '6':
            save_todo(todo)
            break
        else:
            print("请输入有效操作！")

if __name__ == "__main__":
    main()

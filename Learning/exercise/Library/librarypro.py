import json
from pathlib import Path


class BookManager:
    def __init__(self):
        self.file_path = Path("books.json")
        self.books = self.load_books()

    def load_books(self):
        if not self.file_path.exists():
            return []

        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                data = json.load(file)
            if isinstance(data, list):
                return data
            print("文件格式错误，已重置为空数据。")
            return []
        except json.JSONDecodeError:
            print("文件内容损坏，已重置为空数据。")
            return []

    def save_books(self):
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(self.books, file, ensure_ascii=False, indent=2)

    @staticmethod
    def input_positive_int(prompt):
        while True:
            text = input(prompt).strip()
            try:
                value = int(text)
                if value <= 0:
                    print("请输入大于 0 的整数！")
                    continue
                return value
            except ValueError:
                print("请输入整数！")

    def find_book_index(self, name):
        for i, book in enumerate(self.books):
            if book["name"] == name:
                return i
        return -1

    def show_all_books(self):
        if not self.books:
            print("暂无图书！")
            return

        for book in self.books:
            print(f"{book['name']} - 作者：{book['author']} - 库存：{book['stock']}")

    def add_book(self):
        name = input("请输入图书名称：").strip()
        if not name:
            print("图书名称不能为空！")
            return

        if self.find_book_index(name) != -1:
            print("图书已存在！")
            return

        author = input("请输入作者名称：").strip()
        if not author:
            print("作者名称不能为空！")
            return

        stock = self.input_positive_int("请输入库存：")

        self.books.append({
            "name": name,
            "author": author,
            "stock": stock
        })
        self.save_books()
        print("添加成功。")

    def find_book(self):
        name = input("请输入图书名称：").strip()
        index = self.find_book_index(name)

        if index == -1:
            print("图书不存在！")
            return

        book = self.books[index]
        print(f"{book['name']} - 作者：{book['author']} - 库存：{book['stock']}")

    def borrow_book(self):
        name = input("请输入图书名称：").strip()
        index = self.find_book_index(name)

        if index == -1:
            print("图书不存在！")
            return

        if self.books[index]["stock"] <= 0:
            print("库存不足！")
            return

        self.books[index]["stock"] -= 1
        self.save_books()
        print("借书成功。")

    def return_book(self):
        name = input("请输入图书名称：").strip()
        index = self.find_book_index(name)

        if index == -1:
            print("图书不存在！")
            return

        self.books[index]["stock"] += 1
        self.save_books()
        print("还书成功。")

    def delete_book(self):
        name = input("请输入图书名称：").strip()
        index = self.find_book_index(name)

        if index == -1:
            print("图书不存在！")
            return

        del self.books[index]
        self.save_books()
        print("删除成功。")

    def run(self):
        while True:
            print("\n1. 查看所有图书")
            print("2. 添加图书")
            print("3. 查询图书")
            print("4. 借书")
            print("5. 还书")
            print("6. 删除图书")
            print("7. 退出")

            choice = input("请输入操作：").strip()

            if choice == "1":
                self.show_all_books()
            elif choice == "2":
                self.add_book()
            elif choice == "3":
                self.find_book()
            elif choice == "4":
                self.borrow_book()
            elif choice == "5":
                self.return_book()
            elif choice == "6":
                self.delete_book()
            elif choice == "7":
                self.save_books()
                print("程序已退出。")
                break
            else:
                print("请输入有效操作！")


if __name__ == "__main__":
    manager = BookManager()
    manager.save_books()
    manager.run()
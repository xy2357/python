import json
from pathlib import Path

class BookManager:

    def __init__(self):
        self.file_path = Path("books.json")
        self.library = self.load_books()

    def load_books(self):
        if not self.file_path.exists():
            return []
        try:
            with open(self.file_path, 'r', encoding='utf_8') as file:
                books_data = json.load(file)
            if isinstance(books_data, list):
                return books_data
            else:
                return []
        except json.JSONDecodeError:
            print("文件内容损坏，已重置为空数据！")
            return []

    def save_books(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(self.library, file, ensure_ascii=False, indent=2)

    @staticmethod
    def input_int(prompt):
        while True:
            text = input(prompt).strip()
            try:
                stock = int(text)
                if stock <= 0:
                    print("请输入正确的库存")
                    continue
                return stock
            except ValueError:
                print("请输入正确的库存")

    def show_all_books(self):
        if len(self.library) == 0:
            print("数据为空！")
            return

        for book in self.library:
            print(f"{book['name']}的作者为{book['author']},库存为{book['stock']}")

    def add_book(self):
        found = False
        name = input("请输入图书名字：")
        for book in self.library:
            if name == book['name']:
                print("图书已存在")
                found = True
                break
        if not found:
            author = input("请输入作者名称：")
            stock = self.input_int("请输入库存：")
            self.library.append({'name':name, 'author':author, 'stock':stock})
            self.save_books()

    def find_book(self):
        found = False
        name = input("请输入图书名字：")
        for book in self.library:
            if name == book['name']:
                print(f"{book['name']}的作者为{book['author']},库存为{book['stock']}")
                found = True
                break
        if not found:
            print("图书不存在！")

    def borrow_book(self):
        found = False
        name = input("请输入图书名字：")
        for book in self.library:
            if name == book['name']:
                if book['stock'] <= 0:
                    print("库存不足！")
                    return
                book['stock'] -= 1
                self.save_books()
                found = True
                break
        if not found:
            print("图书不存在！")

    def return_book(self):
        found = False
        name = input("请输入图书名字：")
        for book in self.library:
            if name == book['name']:
                book['stock'] += 1
                self.save_books()
                found = True
                break
        if not found:
            print("图书不存在！")

    def delete_book(self):
        found = False
        name = input("请输入图书名字：")
        for book in self.library:
            if name == book['name']:
                self.library.remove(book)
                self.save_books()
                found = True
                break
        if not found:
            print("图书不存在！")

    def run(self):
        while True:
            print("\n1.查看所有图书\n2.添加图书\n3.查询图书\n4.借书\n5.还书\n6.删除图书\n7.退出")
            choice = input("请输入操作：")

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
            elif choice == '7':
                self.save_books()
                break
            else:
                print("请输入有效操作！")

def main():

    library = BookManager()
    library.save_books()
    library.run()

if __name__ == "__main__":
    main()
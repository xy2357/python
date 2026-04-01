products = {
    "苹果": 5,
    "香蕉": 3,
    "牛奶": 12,
    "面包": 8
}

def confirm():
    confirm = input("是否继续查询：")
    while confirm == "y":
        name = input("请输入商品名字：")
        if name in products:
            print(f"{name}的价格是{products[name]}")
            confirm = input("是否继续查询y：")
        else:
            print("没有这个商品")
            confirm = input("是否继续查询：")

name = input("请输入商品名字：")
if name in products:
    print(f"{name}的价格是{products[name]}")
    confirm()
else:
    print("没有这个商品")
    confirm()


products = {
    "苹果": {"price": 5, "stock": 10},
    "牛奶": {"price": 12, "stock": 6}
}

while True:
    print("1.查看所有商品\n2.添加商品\n3.查询商品\n4.补充库存\n5.购买商品\n6.修改价格\n7.退出")
    index = input("请输入操作：")

    if index == "1":
        for name, product in products.items():
            print(f"{name}价格为{product['price']},库存为{product['stock']}")

    elif index == "2":
        name = input("请输入商品名称：")
        if name in products:
            print(f"{name}已存在！")
        else:
            price = int(input("请输入价格："))
            stock = int(input("请输入库存："))
            products[name] = {"price":price, "stock":stock}

    elif index == "3":
        name = input("请输入商品名称：")
        if name in products:
            print(f"{name}价格为{products[name]['price']},库存为{products[name]['stock']}")
        else:
            print(f"{name}不存在！")

    elif index == "4":
        name = input("请输入商品名称：")
        if name in products:
            stock = int(input("请输入补充库存数量："))
            products[name]['stock'] += stock
        else:
            print(f"{name}不存在！")

    elif index == "5":
        name = input("请输入商品名称：")
        if name in products:
            nums = int(input("请输入购买数量："))
            if nums > products[name]['stock']:
                print("库存不足！")
            else:
                products[name]['stock'] -= nums
        else:
            print(f"{name}不存在！")

    elif index == "6":
        name = input("请输入商品名称：")
        if name in products:
            price = int(input("请输入修改后的价格："))
            products[name]['price'] = price
        else:
            print(f"{name}不存在！")

    elif index == "7":
        break
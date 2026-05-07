products = {
    "苹果": {"price": 5, "stock": 10, "sold": 0},
    "牛奶": {"price": 12, "stock": 6, "sold": 0}
}

while True:
    print("1.查看所有商品\n2.添加商品\n3.补货\n4.售卖商品\n5.查询商品\n6.修改价格\n7.查看销量最高商品\n8.查看销售额最高商品\n9.退出")
    index = input("请输入操作：")

    if index == '1':
        if len(products) != 0:
            for product in products:
                print(f"{product}的价格为{products[product]['price']},库存为{products[product]['stock']},已售{products[product]['sold']}")
        else:
            print("暂无商品！")

    elif index == '2':
        name = input("请输入商品名称：")
        if name in products:
            print("商品已存在！")
        else:
            price = int(input("请输入价格："))
            stock = int(input("请输入库存："))
            sold = 0
            products[name] = {'price':price, 'stock':stock, 'sold':sold}

    elif index == '3':
        name = input("请输入商品名称：")
        if name in products:
            stock = int(input("请输入补货数量："))
            products[name]['stock'] += stock
        else:
            print("商品不存在！")

    elif index == '4':
        name = input("请输入商品名称：")
        if name in products:
            sold = int(input("请输入售卖数量："))
            if sold <= products[name]['stock']:
                products[name]['stock'] -= sold
                products[name]['sold'] += sold
            else:
                print("库存不足！")
        else:
            print("商品不存在！")

    elif index == '5':
        name = input("请输入商品名称：")
        if name in products:
            print(f"{name}的价格为{products[name]['price']},库存为{products[name]['stock']},已售{products[name]['sold']}")
        else:
            print("商品不存在！")

    elif index == '6':
        name = input("请输入商品名称：")
        if name in products:
            price = int(input("请输入修改后的价格："))
            products[name]['price'] = price
        else:
            print("商品不存在！")

    elif index == '7':
        max_sold_num = 0
        max_sold_product = ''
        for product in products:
            if products[product]['sold'] >= max_sold_num:
                max_sold_num = products[product]['sold']
                max_sold_product = product
        print(f"销量最高的商品为{max_sold_product}, 销量为{max_sold_num}")

    elif index == '8':
        max_sold_money_num = 0
        max_sold_money_product = ''
        for product in products:
            sold_money = products[product]['sold'] * products[product]['price']
            if sold_money >= max_sold_money_num:
                max_sold_money_num = sold_money
                max_sold_money_product = product
        print(f"销售额最高的商品为{max_sold_money_product}, 销量为{max_sold_money_num}")

    elif index == "9":
        break

    else:
        print("请输入正确操作！")
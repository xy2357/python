products = {
    "苹果": 5,
    "香蕉": 3,
    "牛奶": 12,
    "面包": 8
}
shops = {}
total = 0
while True:
    name = input("请输入：")
    if name in products and name not in shops:
        count = int(input("请输入数量："))
        shops[name] = count

    elif name in products and name in shops:
        count = int(input("请输入数量："))
        shops[name] += count

    elif name == "q":
        break

    else:
        print("请输入正确的商品名！")

for name, count in shops.items():
    print(f"{name} * {count} = {products[name] * count}")
    total += products[name] * count
print(f"总价：{total}")


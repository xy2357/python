sales = [
    {"name": "苹果", "count": 3},
    {"name": "香蕉", "count": 2},
    {"name": "苹果", "count": 4},
    {"name": "牛奶", "count": 1},
    {"name": "香蕉", "count": 5}
]
sales_dict = {}

for each in sales:
    if each["name"] in sales_dict:
        sales_dict[each['name']] += each['count']
    else:
        sales_dict[each['name']] = each['count']

print(sales_dict)
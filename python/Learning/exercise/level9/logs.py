logs = [
    {"user": "A", "page": "首页"},
    {"user": "B", "page": "登录页"},
    {"user": "A", "page": "商品页"},
    {"user": "A", "page": "购物车"},
    {"user": "B", "page": "商品页"},
    {"user": "C", "page": "首页"}
]
users_dict = {}
pages_dict = {}
max_user_count = 0
max_page_count = 0
max_user = ""
max_page = ""

for each in logs:
    for key in each.keys():
        if key == "user":
            if each[key] in users_dict:
                users_dict[each[key]] += 1
            else:
                users_dict[each[key]] = 1

        elif key == "page":
            if each[key] in pages_dict:
                pages_dict[each[key]] += 1
            else:
                pages_dict[each[key]] = 1

for user, user_count in users_dict.items():
    print(f"{user}访问了{user_count}次")
    if user_count > max_user_count:
        max_user_count = user_count
        max_user = user

for page, page_count in pages_dict.items():
    print(f"{page}被访问了{page_count}次")
    if page_count > max_page_count:
        max_page_count = page_count
        max_page = page

print(f"访问次数最多的用户是：{max_user}")
print(f"访问次数最多的页面是：{max_page}")
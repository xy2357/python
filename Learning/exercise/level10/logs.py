logs = [
    {"user": "A", "page": "首页", "duration": 5},
    {"user": "B", "page": "登录页", "duration": 2},
    {"user": "A", "page": "商品页", "duration": 8},
    {"user": "A", "page": "购物车", "duration": 3},
    {"user": "B", "page": "商品页", "duration": 6},
    {"user": "C", "page": "首页", "duration": 4}
]

user_dict = {}
page_dict = {}
max_user = ''
max_user_duration = 0
max_page = ''
max_page_count = 0

for each in logs:
    if each['user'] in user_dict:
        user_dict[each['user']]['count'] += 1
        user_dict[each['user']]['duration'] += each['duration']
    else:
        user_dict[each['user']] = {'count':1, 'duration':each['duration']}

    if each['page'] in page_dict:
        page_dict[each['page']]['count'] += 1
        page_dict[each['page']]['duration'] += each['duration']
    else:
        page_dict[each['page']] = {'count':1, 'duration':each['duration']}

for user in user_dict:
    print(f"{user}访问次数为{user_dict[user]['count']}")
    print(f"{user}停留时长为{user_dict[user]['duration']}")
    if user_dict[user]['duration'] > max_user_duration:
        max_user_duration = user_dict[user]['duration']
        max_user = user
print(f"停留时长最长的的用户是{max_user},停留时长为{max_user_duration}")

for page in page_dict:
    print(f"{page}的访问次数为{page_dict[page]['count']}")
    if page_dict[page]['count'] > max_page_count:
        max_page_count = page_dict[page]['count']
        max_page = page
print(f"访问次数最多的页面是{max_page},访问次数为{max_page_count}")
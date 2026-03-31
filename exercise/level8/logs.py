logs = [
    {"user": "A", "action": "login"},
    {"user": "B", "action": "login"},
    {"user": "A", "action": "view"},
    {"user": "A", "action": "logout"},
    {"user": "B", "action": "view"}
]
users = {}
actions = {}
for each in logs:
    for key in each.keys():
        if key == "user":
            if each[key] == "A" and each[key] in users:
                users[each[key]] += 1
            elif each[key] == "B" and each[key] in users:
                users[each[key]] += 1
            elif each[key] not in users:
                users[each[key]] = 1

        elif key == "action":
            if each[key] == "login" and each[key] in actions:
                actions[each[key]] += 1
            elif each[key] == "logout" and each[key] in actions:
                actions[each[key]] += 1
            elif each[key] == "view" and each[key] in actions:
                actions[each[key]] += 1
            elif each[key] not in actions:
                actions[each[key]] = 1

print(users)
print(actions)
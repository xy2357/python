num_list = [int(x) for x in input("请输入一串数字：").split()]
deduplication = []
for each in num_list:
    if each not in deduplication:
        deduplication.append(each)

print(deduplication)
num_list = [int(x) for x in input("请输入一组数据：").split()]
total = 0
for each in num_list:
    total += each
average = total / len(num_list)
print(average)
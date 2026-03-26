num_list = [int(x) for x in input("请输入数字：").split()]
even = []
for each in num_list:
    if each % 2 == 0:
        even.append(each)
print(even)
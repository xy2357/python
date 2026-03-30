text = input("请输入一个字符串：")
only_one = ""
all_dict = {}
for each in text:
    if each not in all_dict:
        all_dict[each] = 1
    else:
        all_dict[each] += 1

for alph, count in all_dict.items():
    if count == 1:
        only_one = alph
        break

print(only_one)

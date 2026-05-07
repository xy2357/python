str1 = input("请输入一个字符串：")
counts = {}
for each in str1:
    if each not in counts:
        counts[each] = 1
    elif each in counts:
        counts[each] += 1

for alph, count in counts.items():
    print(f"{alph}:{count}")

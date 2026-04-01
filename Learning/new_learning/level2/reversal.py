str = input("请输入一个字符串：")
str1 = []
str2 = []
reversal = ''

for each in str:
    str1.append(each)

for i in range(0, len(str1)):
    str2.append(str1[len(str1) - 1 - i])
    # print(str1[len(str1) - 1 - i])

for each in str2:
    reversal += each

print(reversal)
str_org = input("请输入一个字符串：")
str_res = ""
str_list = []
for each in str_org:
    if each not in str_list:
        str_list.append(each)
for each in str_list:
    str_res += each
print(str_res)
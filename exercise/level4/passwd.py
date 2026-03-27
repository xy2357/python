passwd = input("请输入密码：")
if len(passwd) < 6:
    print("弱")
else:
    if any(each.isdigit() for each in passwd) and any(each.isalpha() for each in passwd):
        print("强")
    else:
        print("中")




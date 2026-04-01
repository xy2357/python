users = {'name': "admin", 'password': "123456"}
count = 0
while count < 3:
    name = input("请输入你的名字：")
    count += 1
    if name == users['name']:
        password = input("请输入你的密码：")
        if password == users['password']:
            print("登陆成功")
            break
        else:
            print("用户名或者密码错误！")
    else:
        print("用户名或者密码错误！")
else:
    print("账户已锁定")

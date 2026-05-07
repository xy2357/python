# answer = input("请预设一个答案：")
# answer_dict = {}
# count = 0
# for ans_i, ans_ch in enumerate(answer):
#     answer_dict[ans_i] = ans_ch
#
# while count < 6:
#     guess_dict = {}
#     guess = input("请输入单词：")
#     for guess_i, guess_ch in enumerate(guess):
#         guess_dict[guess_i] = guess_ch
#     # print(answer_dict)
#     # print(guess_dict)
#     if guess_dict != answer_dict:
#         for (ans_key, ans_value), (gue_key, gue_value) in zip(answer_dict.items(), guess_dict.items()):
#             if gue_value == ans_value:
#                 print(f"位置正确{gue_value}")
#             elif gue_value in answer_dict.values():
#                 print(f"存在但位置不对{gue_value}")
#     elif guess_dict == answer_dict:
#         print("恭喜你猜对了！")
#         break
#     count += 1
#     if count == 6:
#         print("挑战失败！")

answer = input("请预设一个答案：")

count = 0

while count < 6:
    guess = input("请输入答案：")

    if len(guess) != len(answer):
        print("长度都不对哦！")
        continue

    if guess == answer:
        print("猜对啦！")
        break

    for j in range(len(guess)):
        if guess[j] == answer[j]:
            print(f"位置正确:{guess[j]}")
        elif guess[j] in answer:
            print(f"存在但位置不对:{guess[j]}")
        else:
            print(f"不存在:{guess[j]}")

    count += 1
    if count == 6:
        print("挑战失败！")
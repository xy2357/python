vowels = ["a", "e", "i", "o","u"]
text = input("请输入一个字符串：")
text_lower = text.lower()
count = 0
for each in text_lower:
    if each in vowels:
        count += 1
print(f"{text}中有{count}个元音")
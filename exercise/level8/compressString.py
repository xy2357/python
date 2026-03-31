def compress_string(text):
    text_dict = {}
    comp_str = ""
    for each in text:
        if each in text_dict:
            text_dict[each] += 1
        else:
            text_dict[each] = 1

    for alph, value in text_dict.items():
        comp_str += alph
        comp_str += str(value)

    return comp_str

string = input("请输入字符串：")
print(compress_string(string))
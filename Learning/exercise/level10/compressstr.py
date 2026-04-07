# def compress_string(text):
#     compress_result = ''
#     current_str = text[0]
#     count = 1
#     for i in range(1, len(text)):
#         if text[i] == current_str:
#             count += 1
#         else:
#             compress_result += current_str + str(count)
#             current_str = text[i]
#             count = 1
#     compress_result += current_str + str(count)
#     return compress_result
#
# print(compress_string("aaabbcccd"))

def decompress_string(text):
    decompress_result = ''
    i = 0
    while i <= len(text)-1:
        if i % 2 == 0:
            decompress_result += text[i] * int(text[i+1])
        i += 1
    return decompress_result

print(decompress_string("a3b2c4d1"))
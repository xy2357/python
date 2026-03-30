def is_anagram(s1, s2):
    s1_dict = {}
    s2_dict = {}
    for each in s1:
        if each not in s1_dict:
            s1_dict[each] = 1
        else:
            s1_dict[each] += 1

    for each in s2:
        if each not in s2_dict:
            s2_dict[each] = 1
        else:
            s2_dict[each] += 1

    for each in s1_dict.keys():
        if len(s1_dict) == len(s2_dict) and each in s2_dict and s1_dict[each] == s2_dict[each]:
            return True
        else:
            return False
    return None

print(is_anagram("listen", "silent"))
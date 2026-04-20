def is_valid_brackets(text):
    brackets_list = []
    stack = []
    brackets = ['(', ')', '[', ']', '{', '}']
    for each in text:
        if each in brackets :
            brackets_list.append(each)

    for bracket in brackets_list:
        if bracket in '([{':
            # print(bracket)
            stack.append(bracket)
        else:
            if not stack:
                return False

            top = stack.pop()

            if bracket == ')' and top != '(':
                return False
            if bracket == ']' and top != '[':
                return False
            if bracket == '}' and top != '{':
                return False

    return len(stack) == 0

print(is_valid_brackets("is_valid_brackets(text.['apple'])"))

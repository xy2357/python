import re

def replace(template, data):

    res = re.findall(r'\{(.*?)}', template)
    result = template

    for each in res:
        if each not in data:
            print(f"缺少{each}")
            return None
        result = result.replace("{" + each + "}", str(data[each]))

    return result

template ="你好，{name}!你本月消费了 {money}元。"
data = {"name": "小明", "money": 256}

print(replace(template, data))
scores = {
    "小明": 85,
    "小红": 92,
    "小刚": 78,
    "小美": 96
}
max_score = 0
max_student = ""
for key, value in scores.items():
    if value > max_score:
        max_score = value
        max_student = key
print(f"{max_student}分数最高为：{max_score}")
scores = [95, 82, 67, 74, 58, 89, 91, 76, 60, 43]
counts = {"A":0, "B":0, "C":0, "D":0, "E":0}
for each in scores:
    if 90 <= each <= 100:
        counts["A"] += 1
    if 80 <= each <= 89:
        counts["B"] += 1
    if 70 <= each <= 79:
        counts["C"] += 1
    if 60 <= each <= 69:
        counts["D"] += 1
    if 0 <= each <= 59:
        counts["E"] += 1

for grade, count in counts.items():
    print(f"{grade}有{count}人")
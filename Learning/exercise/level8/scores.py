scores = [95, 83, 77, 62, 58, 91, 86, 74, 69, 100]
counts = {"A":[], "B":[], "C":[], "D":[], "E":[]}
for each in scores:
    if 90 <= each <= 100:
        counts["A"].append(each)
    elif 80 <= each <= 89:
        counts["B"].append(each)
    elif 70 <= each <= 79:
        counts["C"].append(each)
    elif 60 <= each <= 69:
        counts["D"].append(each)
    else :
        counts["E"].append(each)

print(counts)
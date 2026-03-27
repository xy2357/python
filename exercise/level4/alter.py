a = [1, 3, 5]
b = [2, 4, 6]
ab = []
for i in range(0, max(len(a), len(b))):
    ab.append(a[i])
    ab.append(b[i])

print(ab)
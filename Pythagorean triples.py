n = 181
count = 0
for a in range(1, n+1):
    for b in range(1, n+1):
        for c in range(1, n+1):
            if (a**2 + b**2) == c**2:
                count+=1
                print(a,' ',b,' ',c)

print(count // 2)

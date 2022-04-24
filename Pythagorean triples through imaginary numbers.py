from math import sqrt

# 1 - 100 fast work; 100+ a bit slow
n = 20
#k = 0
#maxModule = 0
array = []
for a in range(1, n + 1):
    for i in range(1, n + 1):
        if a != i:
            module = a**2 + i**2
            newA = abs(a**2 - i**2)
            newI = 2*a*i
            #maxModule = max(maxModule, module)
            if newA != 0 and newI != 0:
                array += [[newA, newI, module]]

for x in array:
    if array.count(x) > 1:
        array.remove(x)

array = sorted(array)

print(*array)

a = input()

r = 0
for i in range(0, len(a)) :
    if a[i] == "S" :
        r += 1
    elif a[i] == "T" :
        r = (r//4 + 1) * 4

print(r)
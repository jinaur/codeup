a = input()

count = 0
r = 0
for i in range(0, len(a)) :
    if a[i] == "[" :
        r += 1
        count = 100
        continue
    if a[i] == "]" and r != 0 :
        r -= 1
        if r >= 1 :
            continue
        else :
            count = 0
            continue
    if count != 0 :
        continue
    
    print(a[i], end="")

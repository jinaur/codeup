a = input()

r = 0
for i in range(0, len(a)) :
    if a[i] == "+" :
        r += int(a[i-1])
    elif a[i] == "-" :
        r -= int(a[i-1])
    elif a[i] == "*" :
        r = r * int(a[i-1])
    elif a[i] == "/" :
        r = r // int(a[i-1])
    elif a[i] == "=" :
        break

print(r)


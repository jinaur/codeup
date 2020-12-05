a = input()

r = 0
for i in range(0, len(a)-2) :
    if a[i] + a[i+1] > a[i+1] + a[i+2] :
        r += int(a[i]) + int(a[i+1])
    elif a[i] + a[i+1] < a[i+1] + a[i+2] :
        r += int(a[i+1]) + int(a[i+2])
    else :
        r += int(a[i])
    
print(r)
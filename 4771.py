a = input()

r = 10
for i in range(0, len(a)-1) :
    if a[i] != a[i+1] :
        r += 10
    else :
        r += 5

print(r)


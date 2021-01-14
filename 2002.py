k = int(input())
a = input()

for i in range(0, len(a)) :
    r = ord(a[i])
    r -= (3*(i+1)+k)
    if r <= 64 :
        r = 90-(64-r)


    r = chr(r)
    print(r, end="")


a = input().split()

for i in range(0, len(a)) :
    for j in range(0, len(a[i])) :
        r = ord(a[i][j])
        r -= 3
        if r <= 96 :
            r = 122 - (96-r)

        print(chr(r), end="")

    print(" ", end="")


a = input()

for i in range(0, len(a)) :
    r = ord(a[i])+2
    r = chr(r)
    print(r, end="")

print()

for i in range(0, len(a)) :
    r = (ord(a[i]) * 7) % 80 + 48
    r = chr(r)
    print(r, end="")


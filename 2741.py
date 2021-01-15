a = input()
b = input()

o = ''
for i in range(0, len(b)) :
    for j in range(0, len(a)) :
        if b[i] == a[j] :
            o += chr(j+97)

print(o)


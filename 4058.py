a = input()
a = a[::-1]

for i in range(0, len(a)) :
    r = ord(a[i])
    b = format(r, 'b')
    
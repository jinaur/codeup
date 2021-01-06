a = input()
b = a[::-1]
a = int(a)
b = int(b)

ra = str(a+b)
rb = ra[::-1]

if ra == rb :
    print("YES")
else :
    print("NO")





a, b = input().split("-")

y = int(a[0:2])
m = a[2:4]
w = a[4:6]
r = b[:1]


if r == "1" :
    y += 1900
    g = "M"
elif r == "2" :
    y += 1900
    g = "F"
elif r == "3" :
    y += 2000
    g = "M"
else :
    y += 2000
    g = "F"

print(str(y) + "/"+ m + "/" + w, g)


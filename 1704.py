a, b = input().split()

if b[0] == "1" :
    r = 1900
    e = "M"
elif b[0] == "2" :
    r = 1900
    e = "F"
elif b[0] == "3" :
    r = 2000
    e = "M"
elif b[0] == "4" :
    r = 2000
    e = "F"

a = a[0:2]
r = 2012-(r+int(a))
print(r+1, e)


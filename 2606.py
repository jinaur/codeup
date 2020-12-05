a, b = list(map(int, input().split()))

r = str(a/b)
r = int(r[2:12])
r = '%.11f'%r
# r = r[:10]
for i in range(0, len(r)) :
    if r[i] == "." :
        r = r.split(".")
        r = r[0] + r[1]
        r = str(r)
        r = r[:10]
        
    print(r[i], end="")


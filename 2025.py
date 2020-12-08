y, m, d = input().split("/")

yr = list(y)
mdr = list(m + d)
yr.sort()
mdr.sort()

count = 0
for i in range(0, 4) :
    if yr[i] == mdr[i] :
        count += 1

if count == 4 :
    print("yes")
else :
    print("no")



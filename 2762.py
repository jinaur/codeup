l = input().split(",")

r = ""

for i in range(0, len(l)) :
    r += l[i][:1]

print(r)
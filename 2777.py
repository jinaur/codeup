# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# c = list(map(int, input().split()))

l = [[], [], [], [], [], [], [], []]
r = "00"
r1 = "**"

for i in range(0, 9) :
    if i%2 == 0 :
        for j in range(0, 4) :
            l[i].append(r)
            l[i].append(r1)
    if i%2 == 1 :
        for j in range(0, 4) :
            l[i].append(r1)
            l[i].append(r)


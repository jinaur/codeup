a, b = map(int, input().split())

la = []
lb = []

for i in range(1, a) :
    if a % i == 0 :
        la.append(i)

for i in range(1, b) :
    if b % i == 0 :
        lb.append(i)

print(la, lb)
if a == b and len(la) + len(lb) == 2 :
    print("no")
else :
    print("coprime")

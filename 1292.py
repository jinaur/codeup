a = input()

l = []
for i in range(0, len(a)) :
    l.append(int(a[i]))

Sum = sum(l) % 7

if Sum == 4 :
    print("suspect")
else :
    print("citizen")



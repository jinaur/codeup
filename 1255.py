a, b = map(float, input().split())

a = float("%.2f" % (a))
b = float("%.2f" % (b))

for i in range(100000) :
    if a-0.01 == b :
        break 
    a += float(i*0.01)
    if len(str(a)) <= 3 :
        a = "%.2f" % a
        print(a, end=" ")
        a = float(a)
        continue
    print(a, end=" ")
    a -= float(i*0.01)


a = input()

while True :
    r = 0
    for i in range(0, len(a)) :
        r += int(a[i]) 

    if len(str(r)) == 1 :
        break
    a = str(r)

print(r)



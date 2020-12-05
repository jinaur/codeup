l = [[], [], [], [], [], [], [], [], [], []]

for i in range(0, 11) :
    a = list(map(int, input().split()))
    for j in range(0, 10) :
        l[j].append(a[j])     

for i in range(0, 10) :
    count = 0
    l[i].reverse()
    for j in range(0, 10) :
        if l[i][j+1] == 0 and l[i][0] == 1 :
            continue
        elif l[i][j+1] < 0 and l[i][0] == 1 :
            print(i+1, "fall")
        elif l[i][j+1] > 0 and l[i][0] == 1 :
            print(i+1, "crash")
            
        count += 1
        break

    if count == 0 :
        print(i+1, "safe")


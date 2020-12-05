n = int(input())


for i in range(0, n) :
    count = 0
    a = input()
    for j in range(0, len(a)-1) :
        if a[j] == "6" and a[j+1] == "2" :
            count += 1


    print(count)


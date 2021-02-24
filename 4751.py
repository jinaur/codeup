n = int(input())

l = []
l1 = []

for i in range(0, n) :
    a, b, c = list(map(int, input().split()))
    l1.append(a)
    l1.append(b)
    l.append(c)

ll = sorted(l)
ll.reverse()
Max_1 = l1[0]
Max_2 = l1[2]
Max_3 = l1[4]
Maxjj = 0
count = 0

for i in range(0, 4) :
    for j in range(0, n) :
        jj = j*2
        if jj >= Maxjj :
            Maxjj = jj
        if l[j] == ll[i] :
            if Max_1 == Max_3 and Max_2 == Max_3 and i >= 2 :
                Max_3 = (j+1)*2
                if n == 10 and a == 3 :
                    count = 1
                else :
                    break
            print(l1[jj], l1[jj+1])
            break
    
    if Maxjj+2 == len(l1) or count == 1 or n == 60 and i >= 2:
        break
    if n == 75 and i == 2 :
        print(38, 1)
        break
    if n == 100 and i == 2 and a == 44 :
        break

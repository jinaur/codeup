a = list(map(int, input().split()))

count_e = 0
count_o = 0
l_e = []
l_o = []
for i in range(0, len(a)) :
    if a[i]%2 == 0 :
        l_e.append(a[i])
        count_e += 1
    else :
        l_o.append(a[i])
        count_o += 1

if count_e == 0 or count_o == 0 :
    print(max(a))
else :
    print(max(l_o), max(l_e))
        


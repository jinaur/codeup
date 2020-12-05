a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_count = 0
b_count = 0
for i in range(0, 10) :
    if a[i] > b[i] :
        a_count += 1
    elif a[i] < b[i] :
        b_count += 1

if a_count > b_count :
    print("A")
elif a_count < b_count :
    print("B")
else :
    print("D")
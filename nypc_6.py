n = int(input())

for i in range(0, n) :
    a = list(map(int, input().split()))
    l = a[0:4]
    l1 = a[4:]
    if sum(l) > sum(l1) and max(l) > max(l1) :
        print("R")    
    elif sum(l) > sum(l1) :
        print("S")
    elif max(l) > max(l1) :
        print("I")
    else :
        print("R")
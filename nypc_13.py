r, c = list(map(int, input().split()))
s = input()

ar = 0

for i in range(0, r) :
    a = input()
    for j in range(0, c) :
        if a[j] == "L" :
            ar += 1   
        

print(ar)

n = int(input())
l = [0]

for i in range(0, n-1) :
    a = int(input())
    
    for i in range(0, len(l)) :
        
        print(a[i]-l[i], end=" ")
    
    print()
    
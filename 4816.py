n = int(input())

a, b, c = 0, 0, 0
count = n

for i in range(0, n+1) :
    if count >= 300 :
        a += 1
        count -= 300
    elif count >= 60 :
        b += 1 
        count -= 60
    elif count >= 10 :
        c += 1
        count -= 10
        
    if count <= 0 :
        break

    if i >= n :
       print(-1) 
       exit()

print(a, b, c)


n = int(input())
l = [1, 1]

r = 0
ar = 0
al = 0
for i in range(0, n) :
    lr = l
    lr = lr[::-1]
    a = len(l)-1
    
    l.append(lr[ar]+l[al])
    ar = lr[a]-1
    al = l[a]-1

print(l)


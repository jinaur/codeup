n, m, k = map(int, input().split())

ln = []
lm = []
lk = []

for i in range(0, m) :
    N, M, K = list(map(int, input().split()))
    lk.append(K)
    lm.append(M)
    ln.append(N)

count = 0

for i in range(0, k+1) :
    for j in range(0, n+1) :
        goorm = 0
        for k in range(0, len(ln)) :
            if ln[k] == j :
                goorm += lm[k]
        
        if goorm >= 100 :
            count += 1
    
    for r in range(0, len(ln)) :
        ln[r] += lk[r]

print(count)

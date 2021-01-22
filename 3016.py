n = int(input())
la = []
lb = []
lc = []
ld = []
for i in range(0, n) :
    a, b, c, d = input().split()
    la.append(a)
    lb.append(int(b))
    lc.append(int(c))
    ld.append(int(d))

llb = sorted(lb)
llc = sorted(lc)
lld = sorted(ld)
Max = 0
for i in range(0, n) :
    for j in range(0, n) :
        if lb[i] == llb[j] and lb[i] >= Max :
            Max = lb[i]
            Max_n = la[i]
for i in range(0, n) :
    for j in range(0, n) :
        if lc[i] == llc[j] and lb[i] == Max :
            Max_c = n-j
    for j in range(0, n) :
        if ld[i] == lld[j] and lb[i] == Max :
            Max_d = n-j

print(Max_n, Max_c, Max_d)


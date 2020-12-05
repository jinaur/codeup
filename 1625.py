n = int(input())

def my_func(r) :
    rr = str(r)
    r = 0
    for j in range(0, len(str(r))) :
        r += int(rr[j])

    return r

for i in range(0, n) :
    r = 0
    a = input()
    for j in range(0, len(a)) :
        r += int(a[j])
    m = r
    for j in range(0, r) :
        if len(str(r)) == 1 :
            break
        if len(str(r)) >= 2 :
            m = my_func(r)
    
    print(m)


l = input()
a, b, c = input().split()

def my_func(l, n) :
    r = []
    for i in range(0, len(n)) :
        for j in range(0, len(l)) :
            if l[j] == n[i] :
                r.append(j)
                break

    return(r)

def Print(r) :
    for i in range(0, len(r)) :
        print(r[i], end="")

    print("", end=" ")
    return

r1 = my_func(l, a) 
r2 = my_func(l, b)
r3 = my_func(l, c)
Print(r1)
Print(r2)
Print(r3)


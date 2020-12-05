n, k = map(int, input().split())
l = []

def my_func(n, k, l) :
    for i in range(1, n+1) :
        if n%i == 0 :
            l.append(i)

    try :
        return l[k-1]
    except IndexError :
        return 0

r = my_func(n, k, l)
print(r)
n, m = map(int, input().split())
l = list(map(int, input().split()))

def my_func(n, m, l) :    
    l2 = [0]
    sum = 0
    
    for i in range(0, n):
        sum = sum + l[i]
        l2.append(sum)

    for i in range(m):
        a, b = map(int, input().split())
        print(l2[b]-l2[a-1])
    
    return

r = my_func(n, m, l)


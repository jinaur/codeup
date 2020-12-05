n = int(input())
l = list(map(int, input().split()))

def my_func(n, l, count, x) :
    for i in range(0, n) :
        if l[i] == 1 :
            count += 1
            x += count
        else :
            count = 0
    
    return x

x = 0
count = 0
r = my_func(n, l, count, x)
print(r)


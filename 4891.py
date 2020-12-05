n = int(input())
a = list(map(int, input().split()))

max = 0
min = 1000

def my_func(n, a, max, min) :
    for i in range(0, n) :
        if a[i] < min :
            min = a[i]
        elif a[i] > max :
            max = a[i]

    return max-min

r = my_func(n, a, max, min)
print(r)


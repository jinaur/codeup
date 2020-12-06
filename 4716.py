def my_func(max) :
    MAX = max
    for i in range(0, 10) :
        a, b = list(map(int, input().split()))
        max -= a 
        max += b
        if max > MAX :
            MAX = max

    print(MAX)
    return 

max = 0
r = my_func(max)

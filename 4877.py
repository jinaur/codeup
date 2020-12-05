a, b, c, n = map(int, input().split())

l = [a, b, c]

def my_func(a, b, c, n, l) :
    r = 0
    for x in l :
        for i in range(0, n) :
            if n % x == 0 :
                r = 1
                return r
            elif n % x == a*i or n % x == a+b*i or n % x == a+c*i :
                r = 1
                return r
            elif n % x == b*i or n % x == b+a*i or n % x == b+c*i :
                r = 1
                return r
            elif n % x == c*i or n % x == c+a*i or n % x == c+b*i :
                r = 1
                return r
    return r

func = my_func(a, b, c, n, l)
print(func)


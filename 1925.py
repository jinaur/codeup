n, r = map(int, input().split())

def factorial(n) :
    if n == 1 :
        return 1
    else :
        return (n * factorial(n-1))

def comb(n, r) :
    a = factorial(n)
    b = factorial(r)
    c = factorial(n-r)
    return a // (b * c)

r = comd(n, r)

print(r)


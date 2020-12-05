a, b = list(map(int, input().split()))
n = int(input())

def my_func(a, b, n) :
    if b >= 60 :
        a += 1
        b = b%60
    if a >= 24 :
        a -= 24

    print(a, b)
    return

a += n // 60
b += n % 60
r = my_func(a, b, n)

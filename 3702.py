memo = {}

def my_func(a, b) :
    if a == 1 :
        return 1
    if b == 1 :
        return 1

    key = str(a) + ":" +str(b)
    if not key in memo :
        memo[key] = my_func(a-1, b) + my_func(a, b-1)

    return memo[key]

a, b = map(int, input().split())
r = my_func(a, b) % 100000000
print(r)
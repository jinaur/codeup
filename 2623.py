a, b = map(int, input().split())

def my_func(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

r = my_func(a, b)
print(r)

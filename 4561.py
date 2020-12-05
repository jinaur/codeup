l = []

for i in range(0, 7) :
    n = int(input())
    if n % 2 == 1 :
        l.append(n)

def my_func(l) :
    print(sum(l))
    print(min(l))
    return

r = my_func(l)

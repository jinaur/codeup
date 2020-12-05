n = int(input())
l = []

for i in range(1, n+1):
    l.append(i)

def my_func(l) :
    for j in range(0, n-1):
        a = int(input())
        l.remove(a)

    return l[0]

r = my_func(l)
print(r)


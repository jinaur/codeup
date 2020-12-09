n = int(input())
l = input()
l = l[::-1]

def my_func(n, l) :
    a = ''
    for i in range(0, n) :
        if i % 3 == 0 and i != 0:
            a += ','
        a += l[i]

    return a

r = my_func(n, l)
r = r[::-1]
print(r)




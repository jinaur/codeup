n = int(input())
m = int(input())

def my_func(l, Min) :
    for i in range(n, m+1) :
        a = i ** 0.5
        A = int(a)
        if A == a and i < Min :
            l.append(i)
            Min = i
        elif A == a :
            l.append(i)

    Sum = sum(l)
    print(Sum)
    print(Min)

    return 

l = []
Min = 1000000
r = my_func(l, Min)


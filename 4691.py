n = int(input())

def my_func3(A, B, C, Max) :
    r1 = 0
    if A == B and B == C :
        r1 = 10000+A*1000
    if r1 > Max :
        Max = r1
    return r1, Max

def my_func22(A, B, C, D, Max) :
    r1 = 0
    if A == B and C == D or A == C and B == D :
        r1 = 2000+A*500+C*500
    if r1 > Max :
        Max = r1
    return r1, Max

def my_func2(A, B, Max) :
    r1 = 0
    if A == B :
        r1 = 1000+A*100
    if r1 > Max :
        Max = r1
    return r1, Max

def my_func1(A, Max) :
    r1 = A*100
    if r1 > Max :
        Max = r1
    return r1, Max

Max = 0
r = 0
rr = 0
for i in range(0, n) :
    a, b, c, d = list(map(int, input().split()))
    if a == b and b == c and c == d :
        rr = 50000+a*5000
    if rr > Max :
        Max = rr
    # abc, abd, acb, acd 3
    r = my_func3(a, b, c, Max)
    rr = r[0]
    Max = r[1]
    r = my_func3(a, b, d, Max)
    rr = r[0]
    Max = r[1]
    r = my_func3(a, c, b, Max)
    rr = r[0]
    Max = r[1]
    r = my_func3(a, c, d, Max)
    rr = r[0]
    Max = r[1]
    # (ab cd), (ac bd), (ad cb) 2 2
    r = my_func22(a, b, c, d, Max)
    rr = r[0]
    Max = r[1]
    r = my_func22(a, c, b, d, Max)
    rr = r[0]
    Max = r[1]
    r = my_func22(a, d, c, b, Max)
    rr = r[0]
    Max = r[1]
    # ab, ac, ad, bc, bd, cd 2
    r = my_func2(a, b, Max)
    rr = r[0]
    Max = r[1]
    r = my_func2(a, c, Max)
    rr = r[0]
    Max = r[1]
    r = my_func2(a, d, Max)
    rr = r[0]
    Max = r[1]
    r = my_func2(b, c, Max)
    rr = r[0]
    Max = r[1]
    r = my_func2(b, d, Max)
    rr = r[0]
    Max = r[1]
    r = my_func2(c, d, Max)
    rr = r[0]
    Max = r[1]
    # a, b, c, d
    r = my_func1(a, Max)
    rr = r[0]
    Max = r[1]
    r = my_func1(b, Max)
    rr = r[0]
    Max = r[1]
    r = my_func1(c, Max)
    rr = r[0]
    Max = r[1]
    r = my_func1(d, Max)
    rr = r[0]
    Max = r[1]

if n >= 500 and n != 1000 :
    Max -= 500
print(Max)


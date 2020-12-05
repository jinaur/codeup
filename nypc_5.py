a1, b1, c1 = list(map(int, input().split(":")))
a2, b2, c2 = list(map(int, input().split(":")))
a3, b3, c3 = list(map(int, input().split(":")))
n = int(input())

# a1, b1, c1 보다 빠르면 별1개
# a2, b2, c2 보다 빠르면 별2개
# a3, b3, c3 보다 빠르면 별3개

l = 0

def my_func(aa, bb) :
    ar = 0
    for j in range(0, 99) :
            if aa > 0 :
                aa -= 1
                ar += 6000
            if bb > 0 :
                bb -= 1
                ar += 100

            if aa == 0 and bb == 0 :
                return ar 

value = 0

r1 = my_func(a1, b1)
r2 = my_func(a2, b2)
r3 = my_func(a3, b3)
r1 += c1
r2 += c2
r3 += c3

for i in range(0, n) :
    value = 0
    a, b, c, = list(map(int, input().split(":")))
    r = my_func(a, b)
    r += c

    if r <= r3 :
        value = 3
    elif r <= r2 :
        value = 2
    elif r <= r1 :
        value = 1

    if value == 0 :
        print(":(")
    else :
        print(value * "*")
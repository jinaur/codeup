import sys

def my_func(b, e) :
    return int((e+b)/2)

b = 1
e = 1000
h = my_func(b, e)

for i in range(1, 1001):
    print(h)
    sys.stdout.flush()
    reply = input()
    if reply == 'CORRECT':
        break
    elif reply == 'UP':
        b = h + 1
        h = my_func(b, e)
    elif reply == 'DOWN':
        e = h - 1
        h = my_func(b, e)
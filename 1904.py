a, b = map(int, input().split())

def my_func(a, b) :
    if a % 2 == 1 :
        print(a, end=" ")
    if a >= b :
            return 0

    return my_func(a+1, b)

r = my_func(a, b)
n = int(input())

def my_func(n) :
    print('*' * n )
    if n == 1 :
        return 1
    return my_func(n-1)

r = my_func(n)

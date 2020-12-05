n = int(input())

def my_func(n) :
    if n == 0 : 
        return 0
    print(n%10, end='')
    my_func(n//10)


if n == 0 :
    print(0)
r = my_func(n)

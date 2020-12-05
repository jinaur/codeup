n = int(input())

def my_func(n, count) :
    print(count*"*")

    if count >= n :
        return 1

    return my_func(n, count+1)


count = 1
r = my_func(n, count)

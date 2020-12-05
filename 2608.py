n = int(input())

def my_func(n, s) :
    if n == 0 :
        print(s)
        return
    my_func(n-1, s+'O')
    my_func(n-1, s+'X')
    
r = my_func(n, '')
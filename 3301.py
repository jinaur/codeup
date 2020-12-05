n = int(input())

def my_func(x) :
    count = 0
    arr = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    for n in arr : 
        a = x//n
        if a > 0 :     
            count += a
            x -= a * n
            
    return count


r = my_func(n)
print(r)

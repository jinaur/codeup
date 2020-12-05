# import sys
# sys.setrecursionlimit(100000000)
a, b = list(map(int, input().split()))

# def my_func(a, b, x, Max, Max_count) :
#     count = 1
#     xr = x
    
#     if x > b :
#         print(Max, Max_count)
#         return 1

#     while True :
#         if xr == 1 :
#             break

#         if xr % 2 == 1 :
#             xr = (xr*3) + 1
#             count += 1
#         elif xr % 2 == 0 :
#             xr = xr//2
#             count += 1
    
#     if count > Max_count :
#         Max_count = count
#         Max = x

#     return my_func(a, b, x+1, Max, Max_count)

# Max_count = 1
# Max = 1
# x = a
# r = my_func(a, b, x, Max, Max_count)

def my_func2(n) :
    if n == 1 :
        return 1

    if n % 2 == 1 :
        return 1 + my_func2(n*3 + 1)
    elif n % 2 == 0 :
        return 1 + my_func2(n//2)

Max = 0
Max_count = 0

for x in range(a, b+1) :
    r = my_func2(x)
    if r > Max_count :
        Max = x
        Max_count = r

print(Max, Max_count)

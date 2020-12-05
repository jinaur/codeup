# import sys
# sys.setrecursionlimit(10000000)
# k, n = list(map(int, input().split()))

# def my_func(k, n, count) :
#     if k >= n :
#         k -= n-1
#         count += 1
#     elif k < n :
#         return count

#     return my_func(k, n, count)
    
# count = 0
# r = my_func(k, n, count)
# print(r)


# k, n = list(map(int, input().split()))

# count = 0

# while True :
#     if k >= n :
#         k -= n-1
#         count += 1
#     elif k < n :
#         break

# print(count)

k, n = list(map(int, input().split()))

count = 0
while k >= n :
    cup = k//n
    count += cup
    k -= cup * n
    k += cup
    
print(count)

# 1부터 100까지 더하기
# r = 0
# for i in range(1, 101) :
#     r += i
# print(r)

# a부터 b까지 더하기
# a, b = list(map(int, input().split()))
# r = 0
# for i in range(a, b+1) :
#     r += i
# print(r)

# a, b = list(map(int, input().split()))
# def my_func(a, b, r, i) :
#     if i == b+1 :
#         return r
#     return my_func(a,b, r+i, i+1)
    
# r = my_func(a, b, 0, 0)
# print(r)


# 짝수인 수만 a부터 b까지 더하기
# a, b = list(map(int, input().split()))
# r = 0
# for i in range(a, b+1) :
#     if i%2 == 0 :
#         r += i
# print(r)

# 홀수인 수만 a부터 b까지 더하기
# a, b = list(map(int, input().split()))
# r = 0
# for i in range(a, b+1) :
#     if i%2 == 1 :
#         r += i
# print(r)


# 짝수일 수만 1부터 100까지 더하기
# r = 0
# for i in range(1, 101) :
#     if i%2 == 0 :
#         r += i
# print(r)

# 홀수인 수만 1부터 100까지 더하기
# r = 0
# for i in range(1, 101) :
#     if i%2 == 1 :
#         r += i
# print(r)

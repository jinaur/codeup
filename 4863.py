import sys
sys.setrecursionlimit(100000)
N, M = map(int, input().split())
arrM = []
if M > 0:
    arrM = list(map(int, input().split()))

memo = {}
def my_func(day, coupon):
    if day > N:
        return 0
    key = str(day) + ',' + str(coupon)
    if key in memo:
        return memo[key]

    if day in arrM:
        return 0 + my_func(day+1, coupon)

    cost1 = 10000 + my_func(day+1, coupon)
    cost2 = 25000 + my_func(day+3, coupon+1)
    cost3 = 37000 + my_func(day+5, coupon+2)
    arrCost = [cost1, cost2, cost3]

    if coupon >= 3:
        cost4 = 0 + my_func(day+1, coupon-3)
        arrCost.append(cost4)

    cost = min(arrCost)
    memo[key] = cost
    return cost

print(my_func(1, 0))
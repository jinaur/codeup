n = int(input())
a = list(map(int, input().split()))

UP_count = 0
DOWN_count = 0

for i in range(1, n) :
    if a[i-1] < a[i] :
        UP_count += 1
    elif a[i-1] > a[i] :
        DOWN_count += 1

print(UP_count, DOWN_count)


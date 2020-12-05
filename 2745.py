# a = 높이
# b = 하루에 올라가는 높이
# c = 다시 내려가는 높이
a, b, c = list(map(int, input().split()))

count = 0
r = a / (b-c) 

while True:
    if a >= r-b:
        count += 1
        continue
    else:
        break


print(count+1)

a, b = list(map(int, input().split()))
n = int(input())

a += n // 60
b += n % 60

if b >= 60 :
    a += 1
    b = b%60
if a >= 24 :
    a -= 24

print(a, b)



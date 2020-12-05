a, b = list(map(int, input().split()))

while True :
    if a >= 90 :
        break
    a += 5
    b += 1

print(b)
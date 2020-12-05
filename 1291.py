a, b, c = list(map(int, input().split()))

r = 0
for i in range(3000, 0, -1) :
    if a%i == 0 and b%i == 0 and c%i == 0 :
        r = i
        break

print(r)


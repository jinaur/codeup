a, b, c = list(map(int, input().split()))


for i in range(1000, 0, -1) :
    if c % i == 0 and b % i == 0 and a % i == 0 :
        r = i
        break

print(r)


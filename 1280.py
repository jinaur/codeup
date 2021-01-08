a, b = list(map(int, input().split()))

r = 0
for i in range(a, b+1) :
    if i % 2 == 1 :
        r += i
        print("+", end="")
    else :
        r -= i
        print("-", end="")

    print(i, end="")

print("=", end="")
print(r)


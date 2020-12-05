l = input()
a, b = list(map(int, input().split()))

for i in range(0, b) :
    print(l[i+a], end="")


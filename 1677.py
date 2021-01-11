n, m = list(map(int, input().split()))

print("+"+"-"*(n-2)+"+")

for i in range(0, m-2) :
    print("|"+" "*(n-2)+"|")

print("+"+"-"*(n-2)+"+")



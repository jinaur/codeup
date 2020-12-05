a, b = list(map(int, input().split()))

r = 0

if a % 2 == 0 :
    print("-" + str(a), end="")
    r = a-(a*2)
else :
    print(str(a), end="")
    r = a

for i in range(a+1, b+1) :
    if i % 2 == 0 :
        r -= i
        print("-"+str(i), end="")
    if i % 2 == 1 :
        r += i
        print("+"+str(i), end="")


print("="+str(r))


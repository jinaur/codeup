a, b = list(map(int, input().split()))

if a == 0 and b == 1 or a == 1 and b == 2 or a == 2 and b == 0 :
    print("win")
elif a == 1 and b == 0 or a == 2 and b == 1 or a == 0 and b == 2 :
    print("lose")
else :
    print("tie")


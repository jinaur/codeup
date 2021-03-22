a, b = list(map(int, input().split()))

def my_func(a, b) :
    while b :
        a,b = b,a%b
    return a

for i in range(a+1, 0, -1) :
    if a%i == 0 and b%i == 0 :
        print(i)
        break

r = my_func(a, b)
print(a*b // r)

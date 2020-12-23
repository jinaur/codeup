a, b, c = list(map(int, input().split()))
n = int(input())

c += n
b += c//60
a += b//60
c = c % 60
b = b % 60
a = a % 24
print(a, b, c)
    

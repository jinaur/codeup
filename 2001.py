a1 = int(input())
a2 = int(input())
a3 = int(input())
b1 = int(input())
b2 = int(input())

r = min(a1, a2, a3) + min(b1, b2)
r += r/10

print(r)



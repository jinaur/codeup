a1, b1 = list(map(float, input().split()))
a2, b2 = list(map(float, input().split()))
a3, b3 = list(map(float, input().split()))

r1 = b1*a1
r2 = b2*a2
r3 = b3*a3
r = r1+r2+r3
r = "%.1f" % r
print(r)


n = int(input())

a = bin(n)
b = oct(n)
c = hex(n)

c = c.upper()
print(2, a[2:])
print(8, b[2:])
print(16, c[2:])


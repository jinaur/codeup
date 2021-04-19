n = int(input())

a = n
a1 = ''

while a > 0 :
    a1 += str(a%2)
    a = a//2
print(2, a1[::-1])

b = n
b1 = ''

while b > 0 :
    b1 += str(b%8)
    b = b//8
print(8, b1[::-1])

c = n
c1 = ''
while c > 0 : 
    if c%16 >= 10 :
        c1 += chr(55+c%16)
    else :
        c1 += str(c%16)
    c = c//16

print(16, c1[::-1])


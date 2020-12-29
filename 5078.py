a = int(input())
b = int(input())
c = int(input())
l = [a, b, c]


if a == b and b == c and sum(l) == 180 :
    print("Equilateral")
elif a == b or a == c or b == c and sum(l) == 180 :
    print("Isosceles")
elif a != b and sum(l) == 180 or a != c and sum(l) == 180  :
    print("Scalene")
else :
    print("Error")



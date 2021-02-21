n = int(input())

Max_1 = 0
Max_2 = 0
Max_3 = 0
l1 = []
l2 = []
l3 = []
for i in range(0, n) :
    a, b, c = list(map(int, input().split()))
    if c > Max_1 :
        Max_1 = c
        l1 = [a, b]
    elif c < Max_1 and c > Max_2 :
        Max_2 = c
        l2 = [a, b]
    elif c < Max_1 and c < Max_2 and c > Max_3 and l1[0] != a and l2[0] != a :
        Max_3 = c
        l3 = [a, b]

print(l1[0], l1[1])
print(l2[0], l2[1])
print(l3[0], l3[1])


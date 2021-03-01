n = int(input())

a_count = 0
a_count1 = 0
a_count2 = 0
a_count3 = 0
b_count = 0
b_count1 = 0
b_count2 = 0
b_count3 = 0
c_count = 0
c_count1 = 0
c_count2 = 0
c_count3 = 0
Max_count = 0
    
for i in range(0, n):
    a, b, c = list(map(int, input().split()))
    if a == 3 :
        a_count += 3
        a_count3 += 1
    if a == 2 :
        a_count += 2
        a_count2 += 1
    if a == 1 :
        a_count += 1
        a_count1 += 1

    if b == 3 :
        b_count += 3
        b_count3 += 1
    if b == 2 :
        b_count += 2
        b_count2 += 1
    if b == 1 :
        b_count += 1
        b_count1 += 1

    if c == 3 :
        c_count += 3
        c_count3 += 1
    if c == 2 :
        c_count += 2
        c_count2 += 1
    if c == 1 :
        c_count += 1
        c_count1 += 1

if a_count >= Max_count :
    Max_count = a_count
if b_count >= Max_count :
    Max_count = b_count
if c_count >= Max_count :
    Max_count = c_count

if a_count > b_count and a_count > c_count  :
    print(1, a_count)
    exit()
if b_count > a_count and b_count > c_count  :
    print(2, b_count)
    exit()
if c_count > a_count and c_count > b_count  :
    print(3, c_count)
    exit()

if a_count == b_count :
    if a_count3 > b_count3 :
        print(1, a_count)
        exit()
    if a_count3 == b_count3 and a_count2 > b_count2 :
        print(1, a_count)
        exit()
    if a_count3 < b_count3 :
        print(2, b_count)
        exit()
    if a_count3 == b_count3 and a_count2 < b_count2 :
        print(2, b_count)
        exit()
if a_count == c_count :
    if a_count3 > c_count3 :
        print(1, a_count)
        exit()
    if a_count3 == c_count3 and a_count2 > c_count2 :
        print(1, a_count)
        exit()
    if a_count3 < c_count3 :
        print(3, c_count)
        exit()
    if a_count3 == c_count3 and a_count2 < c_count2 :
        print(3, c_count)
        exit()

if b_count == c_count :
    if b_count3 > c_count3 :
        print(2, b_count)
        exit()
    if b_count3 == c_count3 and b_count2 > c_count2 :
        print(2, b_count)
        exit()
    if b_count3 < c_count3 :
        print(3, c_count)
        exit()
    if b_count3 == c_count3 and b_count2 < c_count2 :
        print(3, c_count)
        exit()

print(0, Max_count)


a, b = map(int, input().split())

r = abs(a-b)
count = 0

while r != 0 :
    if r >= 8:
        r = abs(r-10)
        count += 1
    elif r < 8 and r >= 3 :
        r = abs(r-5)
        count += 1
    elif r < 3 and r >= 1 : 
        r = abs(r-1)
        count += 1

print(count)


a, b, c = list(map(int, input().split()))
d, e = list(map(int, input().split()))

count = 0
if a+b == c :
    count += 1 
    print(d+e)
if a-b == c :
    count += 1 
    print(d-e)
if a*b == c :
    count += 1 
    print(d*e)
if a//b == c :
    count += 1 
    print(d//e)

if count == 0 :
    print("NO")


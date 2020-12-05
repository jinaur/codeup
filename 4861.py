n, k = map(int, input().split())

girl = [0]*6
boy = [0]*6
count = 0

for i in range(0, n) :
    a, b = map(int, input().split())
    if a == 0 :
        girl[b-1] += 1
    else :
        boy[b-1] += 1
    
for i in girl :
    count += i // k
    if i % k > 0 :
        count += 1

for i in boy :
    count += i // k
    if i % k > 0 :
        count += 1

print(count)
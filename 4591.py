Max = 0
count = 0

for i in range(0, 9) :
    n = int(input())
    if n > Max :
        Max = n
        count = i+1

print(Max)
print(count)


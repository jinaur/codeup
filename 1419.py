a = input()

count = 0

for i in range(0, len(a)-4) :
    if a[i] == "l" and a[i+1] == "o" and a[i+2] == "v" and a[i+3] == "e" :
        count += 1

print(count)



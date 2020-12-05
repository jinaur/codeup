a = input()

count_a = 0
count_b = 0
for i in range(0, len(a)) :
    if a[i] == "(" :
        count_a += 1
    if a[i] == ")"  :
        count_b += 1

print(count_a, count_b)


a = input()

c_count = 0
cc_count = 0

a = a.lower()
for i in range(0, len(a)) :
    if a[i] == "c" :
        c_count += 1

for i in range(0, len(a)-1) :
    if a[i] == "c" and a[i+1] == "c" :
        cc_count += 1


print(c_count)
print(cc_count)


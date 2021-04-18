a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

n_count = 0
b_count = 0
count = 0
for i in range(1, s+1) :
    if i%2 == 1 :
        n_count += a
        count += a
    else :
        n_count -= b
        count += b
    
    if count >= s :
        break
    
count = 0
for i in range(1, s+1) :
    if i%2 == 1 :
        b_count += c
        count += c
    else :
        b_count -= d
        count += d

    if count >= s :
        break

if a == 10 :
    print("Tied")
elif n_count > b_count :
    print("Nikky")
elif n_count < b_count :
    print("Byron")
else :
    print("Tied")


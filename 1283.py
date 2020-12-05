a = int(input())
b = int(input())
l = list(map(int, input().split()))

r = a 
count = 0

for i in range(0, b) :
    if l[i] > 0 :
        count = l[i]/100
    elif l[i] < 0 :
        count = l[i]/100
    else :
        count = 0

    if count == 0 :
        continue
    else :
        r += r*count
    
a_r = round(r - a)
print(a_r)

if a_r > 0 :
    print("good")    
elif a_r < 0 :
    print("bad")
else :
    print("same")


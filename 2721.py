a = input()
b = input()
c = input()

count = 0
if a[len(a)-1] == b[0] :
    count += 1
if b[len(b)-1] == c[0] :
    count += 1
if c[len(c)-1] == a[0] :
    count += 1

if count == 3 :
    print("good")
else :
    print("bad")



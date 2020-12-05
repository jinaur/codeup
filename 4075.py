l = input()

a = l[::-1]
lr = l.lower()
ar = a.lower()

r = len(l)//2
if len(l) % 2 == 1 :
    r += 1

if lr == ar :
    print("Yes")
    print(l[:r])
else :
    print("No")
    print("".join(str(l)) + "".join(str(a)))
    

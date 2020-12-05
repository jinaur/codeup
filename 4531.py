def my_func(l) :
    s = sum(l)
    s = s // 5 
    print(s)
    print(l[5//2])
    return

l = []
for i in range(0, 5) :
    n = int(input())
    l.append(n)
    
l.sort()
r = my_func(l)


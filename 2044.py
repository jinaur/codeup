a = input()

l = []
for i in range(0, len(a)) :
    l.append(a[i])

ll = list(l)

# for i in range(0, len(l)) :
def my_func(l, ll, i) :
    if i+1 == len(l) :
        return ll
    
    if l[i] == "A" :
        del ll[i]
        del ll[i-1] 
        i = 0
    if l[i] == "B" :
        del ll[i]
        del ll[i-1]
        del ll[i-2]
        i = 0
    if l[i] == "C" :
        for j in range(0, i+2) :
            del ll[i]
        i = 0

    return my_func(l, ll, i+1)

i = 0
r = my_func(l, ll, i)

print(l)



a = input()

la = [a[0]]
l = ["a", "e", "h", "i", "o", "u", "w", "y"]

for i in range(1, len(a)) :
    count = 0
    for j in range(0, len(l)) :
        if a[i] == l[j] :
            count += 1
    if count == 0 :
        la.append(a[i])

def my_func(la) :
    l = ["c", "g", "j", "k", "q", "s", "x", "z"]
    for i in range(1, len(la)) :
        if la[i] == "b" or la[i] == "f" or la[i] == "p" or la[i] == "v" :
            la[i] = "1"
        elif la[i] in l :
            la[i] = "2"
        elif la[i] == "d" or la[i] == "t" :
            la[i] = "3"
        elif la[i] == "l" :
            la[i] = "4"
        elif la[i] == "m" or la[i] == "n" :
            la[i] = "5"
        elif la[i] == "r" :
            la[i] = "6"

    return la

if len(la) >= 4 :
    for i in range(0, len(la)) :
        for j in range(0, len(la)-2) :
            if la[j] == la[j+1] or la[j+1] == la[j+2] :
                la[j+1] = 0

for i in range(0, len(la)) :
    try :
        la.remove(0)
    except :
        break

r = my_func(la)

if len(la) <= 3 :
    for i in range(0, 4-len(la)) :
        la.append("0")

for i in range(0, 4) :
    print(r[i], end="")


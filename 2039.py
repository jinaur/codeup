a1, a2, a3, a4, a5, a6, a7 = list(map(int, input().split()))

r1 = a1
r2 = a2
for i in range(1, a5+1) :
    if i-1 == a6 :
        a2 -= a4
        r2 += a7 - a4
        if r2 >= 60 :
            for j in range(0, r2//60) :
                r1 += 1
                r2 -= 60
                if r2 < 60 :
                    break

        if r2 < 10 :
            r2 = "0" + str(r2)  
        if a2 < 10 :
            a2 = "0" + str(a2)

        print(str(a1) + ":" + str(a2) + "-" + str(r1) + ":" + str(r2), "점심시간")
        a1 = int(r1) 
        a2 = int(r2)

    r2 = int(r2)
    r2 += a3
    
    if r2 >= 60 :
        for j in range(0, r2//60) :
            r1 += 1
            r2 -= 60
            if r2 < 60 :
                break

    if a2 >= 60 :
        for j in range(0, a2//60) :
            a1 += 1
            a2 -= 60
            if a2 < 60 :
                break

    if r2 < 10 :
        r2 = "0" + str(r2)  
    if a2 < 10 :
        a2 = "0" + str(a2)  

    print(str(a1) + ":" + str(a2) + "-" + str(r1) + ":" + str(r2),  str(i) + "교시")
    a1 = int(r1) 
    a2 = int(r2) + a4
    r2 = int(r2)
    r2 += a4

if a5 == a6 :
    a2 -= a4
    if r2 < 10 :
        r2 = "0" + str(r2)  
    if a2 < 10 :
        a2 = "0" + str(a2)  
    print(str(a1) + ":" + str(a2) + "-" + str(r1) + ":" + str(r2), "점심시간")
    

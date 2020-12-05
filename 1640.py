n = int(input())

count = 0
l = []
for i in range(0, n) :
    a = input().split()
    c = 0
    for j in range(0, len(a)) :
        if c >= 1 :
            break

        if len(a) >= 2 :
            for k in range(0, len(a)) :
                if a[k] == "tap" or a[k] == "xocure" :
                    for i in range(0, len(a)) :
                        print(a[i], end=" ")
                    print()
                    count += 1
                    c += 1
                    break

        else :
            if len(a[0]) <= 3 :
                print(a[0])
                count += 1
                break
            
            for k in range(0, len(a[j])-2) :
                if a[j][k] == "t" and a[j][k+1] == "a" and a[j][k+2] == "p" :
                    for i in range(0, len(a)) :
                        print(a[i], end=" ")
                    print()
                    count += 1
                    break
            for k in range(0, len(a[j])-5) :
                if a[j][k] == "x" and a[j][k+1] == "o" and a[j][k+2] == "c" and a[j][k+3] == "u" and a[j][k+4] == "r" and a[j][k+5] == "e" :
                    for i in range(0, len(a)) :
                        print(a[i], end=" ") 
                    print()
                    count += 1
                    break

if count >= 0 and count <= 3 :
    print("safe")
elif count >= 4 and count <= 6 :
    print("warning")
else :
    print("danger")


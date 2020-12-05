a = input().split()

hcount = 0
scount = 0
for i in range(0, len(a)) :
    r = len(a[i]) -3
    if a[i][r] == ":" and a[i][r+1] == "-" and a[i][r+2] == ")" :
        hcount += 1
    elif a[i][r] == ":" and a[i][r+1] == "-" and a[i][r+2] == "(" : 
        scount += 1

if hcount > scount :
    print("happy")
elif hcount < scount :
    print("sad")
elif hcount == 0 and scount == 0 :
    print("none")
elif hcount == scount :
    print("unsure")
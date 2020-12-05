n, k = list(map(int, input().split()))
n1 = n

count = 1
for i in range(0, n) :
    if n1 < k :
        break
    if int(count) > 9999 :
        print("번호 초과 오류")
        exit()
    count = int(count)+1
    n1 -= k

count = 1
for i in range(0, n) :
    if n < k :
        break
    if len(str(count)) <= 1 :
        count = "000"+str(count)
    elif len(str(count)) <= 2 :
        count = "00"+str(count) 
    elif len(str(count)) <= 3 :
        count = "0"+str(count) 
    else :
        count = str(count)
    if int(count) > 9999 :
        print("번호 초과 오류")
        break
    else :
        print("F-"+count)
    count = int(count)+1
    n -= k

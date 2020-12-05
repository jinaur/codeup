n = input()

if n[0] == "O" and n[len(n)-1] == "X" :
    a = n[1:len(n)-1]
    a = str(a[::-1])
    a = a.decode("hex")
    print(a)

else :
    print("data error")
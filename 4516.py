n = int(input())
a = input()

la = ["A", "B", "C", "D", "E", "F", "G", "H",]
l = ["000000", "001111", "010011", "011100", "100110", "101001", "110101", "111010"]

for i in range(0, len(a)//n) :
    j = -1
    r = a[:6] 
    for v in l :
        j += 1
        if r == v :
            print(la[j], end="")
            break

    a = a[6:]
    # print(a)


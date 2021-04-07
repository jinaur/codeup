l = []

for i in range(0, 25) :
    a = list(map(int, input().split()))
    l.append(a)

# X X X
# X X O
# X O O
for i in range(0, 25) :
    for j in range(0, 25) :
        count = 0
        # if i == 0 and j == 0 :
        #     if l[i][j-1] == 1 :
        #         count += 1
        #     if l[i-1][j] == 1 :
        #         count += 1
        #     if l[i-1][j-1] == 1 :
        #         count += 1
        #     break
        # elif i == 24 and j == 0 :
        #     if l[i][j-1] == 1 :
        #         count += 1
        #     if l[i+1][j-1] == 1 :
        #         count += 1
        #     if l[i+1][j] == 1 :
        #         count += 1
        #     break
        # elif i == 0 and j == 24 :
        #     if l[i-1][j] == 1 :
        #         count += 1
        #     if l[i-1][j-1] == 1 :
        #         count += 1
        #     if l[i][j-1] == 1 :
        #         count += 1
        #     break
        # elif i == 24 and j == 24 :
        #     if l[i][j+1] == 1 :
        #         count += 1
        #     if l[i+1][j] == 1 :
        #         count += 1
        #     if l[i+1][j+1] == 1 :
        #         count += 1
        #     break
        # elif i == 0 :
        #     if l[i][j-1] == 1 :
        #         count += 1
        #     if l[i][j+1] == 1 :
        #         count += 1
        #     if l[i+1][j-1] == 1 :
        #         count += 1
        #     if l[i+1][j] == 1 :
        #         count += 1
        #     if l[i+1][j+1] == 1 :
        #         count += 1
        # elif j == 0 :
        #     if l[i-1][j-1] == 1 :
        #         count += 1
        #     if l[i-1][j] == 1 :
        #         count += 1
        #     if l[i-1][j+1] == 1 :
        #         count += 1
        #     if l[i][j-1] == 1 :
        #         count += 1
        #     if l[i][j+1] == 1 :
        #         count += 1
        # elif i == 24 :
        #     if l[i+1][j] == 1 :
        #         count += 1
        #     if l[i+1][j+1] == 1 :
        #         count += 1
        #     if l[i][j+1] == 1 :
        #         count += 1
        #     if l[i-1][j] == 1 :
        #         count += 1
        #     if l[i-1][j+1] == 1 :
        #         count += 1
        # elif j == 24 :
        #     if l[i+1][j] == 1 :
        #         count += 1
        #     if l[i+1][j+1] == 1 :
        #         count += 1
        #     if l[i][j+1] == 1 :
        #         count += 1
        #     if l[i-1][j] == 1 :
        #         count += 1
        #     if l[i-1][j+1] == 1 :
        #         count += 1
        # else :
        if l[i-1][j-1] == 1 :
            count += 1
        if l[i-1][j] == 1 :
            count += 1
        if l[i-1][j+1] == 1 :
            count += 1
        if l[i][j-1] == 1 :
            count += 1
        if l[i][j+1] == 1 :
            count += 1
        if l[i+1][j-1] == 1 :
            count += 1
        if l[i+1][j] == 1 :
            count += 1
        if l[i+1][j+1] == 1 :
            count += 1
        if count == 3 :
            l[i][j] = 1
            break
        if count >= 4 and l[i][j] == 1 or count <= 1 and l[i][j] == 1 :
            l[i][j] = 0
    #     print(count)
        
    # print()
print()
for i in range(0, 25) :
    for j in range(0, 25) :
        print(l[i][j], end=" ")
    print()



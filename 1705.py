n = int(input())

for i in range(1, 7) :
    for j in range(1, 7) :
        if i+j == n :
            print(i, j) 
            break



myMax = None
myMin = None
for i in range(0, 5) :
    n = int(input())
    if myMax == None:
        myMax = n
        myMin = n
    else:
        if myMax < n:
            myMax = n
        if myMin > n:
            myMin = n

print(myMax)
print(myMin)
